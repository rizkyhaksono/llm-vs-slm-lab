"""Benchmark helpers: latency, peak RAM, token counting.

Notebook benchmark side-by-side (02.04) pakai modul ini supaya konsistensi
metrik antar percobaan.
"""
from __future__ import annotations

import gc
import time
import tracemalloc
from contextlib import contextmanager
from dataclasses import dataclass
from statistics import median
from typing import Callable, Iterator


@dataclass
class BenchmarkResult:
    label: str
    latency_ms: float          # median across runs
    latency_ms_min: float
    latency_ms_max: float
    peak_ram_mb: float
    output_tokens: int | None = None
    output_text: str | None = None
    extra: dict | None = None

    def as_dict(self) -> dict:
        return {
            "label": self.label,
            "latency_ms": round(self.latency_ms, 1),
            "latency_ms_min": round(self.latency_ms_min, 1),
            "latency_ms_max": round(self.latency_ms_max, 1),
            "peak_ram_mb": round(self.peak_ram_mb, 1),
            "output_tokens": self.output_tokens,
            **(self.extra or {}),
        }


@contextmanager
def measure_peak_ram() -> Iterator[Callable[[], float]]:
    """Context manager untuk track peak RAM (MB) selama block.

    Pakai tracemalloc — measure Python object allocation, BUKAN total proses.
    Untuk angka full process, lihat `psutil.Process().memory_info().rss`.
    Yang penting bukan absolute angka, tapi konsisten antar percobaan.

    Usage:
        with measure_peak_ram() as get_peak:
            do_something()
        print(f"peak: {get_peak()} MB")
    """
    gc.collect()
    tracemalloc.start()
    try:
        yield lambda: tracemalloc.get_traced_memory()[1] / (1024 * 1024)
    finally:
        tracemalloc.stop()


def run_with_timing(
    func: Callable[[], str],
    label: str,
    n_runs: int = 3,
    output_token_counter: Callable[[str], int] | None = None,
) -> BenchmarkResult:
    """Run `func()` n_runs kali, return median latency + peak RAM dari run terakhir.

    Args:
        func: callable tanpa args yang return string output (mis. response text).
        label: nama eksperimen untuk display.
        n_runs: berapa kali ulang. Default 3, ambil median.
        output_token_counter: optional, fungsi yang count token dari output text.

    Why median, not mean: latency CPU sering punya outlier dari thermal throttling
    atau GC pause. Median lebih stabil.
    """
    latencies: list[float] = []
    last_output: str | None = None

    for i in range(n_runs):
        gc.collect()
        if i == n_runs - 1:
            with measure_peak_ram() as get_peak:
                t0 = time.perf_counter()
                last_output = func()
                t1 = time.perf_counter()
                peak = get_peak()
        else:
            t0 = time.perf_counter()
            last_output = func()
            t1 = time.perf_counter()
        latencies.append((t1 - t0) * 1000.0)

    out_tokens = (
        output_token_counter(last_output)
        if output_token_counter and last_output is not None
        else None
    )

    return BenchmarkResult(
        label=label,
        latency_ms=median(latencies),
        latency_ms_min=min(latencies),
        latency_ms_max=max(latencies),
        peak_ram_mb=peak,
        output_tokens=out_tokens,
        output_text=last_output,
    )


def estimate_cost_usd(
    input_tokens: int,
    output_tokens: int,
    cost_per_1k_input: float = 0.05 / 1000,
    cost_per_1k_output: float = 0.08 / 1000,
) -> float:
    """Estimasi biaya untuk 1 panggilan API.

    Default rate dari Groq llama-3.1-8b-instant (per Mei 2026).
    Update angka kalau provider ubah harga atau ganti model.
    """
    return (
        input_tokens * cost_per_1k_input
        + output_tokens * cost_per_1k_output
    )
