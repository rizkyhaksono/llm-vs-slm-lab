"""Matplotlib styling konsisten antar notebook."""
from __future__ import annotations

import matplotlib.pyplot as plt


def setup_style() -> None:
    """Panggil sekali di awal notebook untuk styling konsisten.

    Pilihan default sengaja simple — kita prioritas readability di GitHub render.
    """
    plt.rcParams.update({
        "figure.figsize": (8, 4),
        "figure.dpi": 100,
        "axes.spines.top": False,
        "axes.spines.right": False,
        "axes.grid": True,
        "grid.alpha": 0.3,
        "font.size": 11,
    })


# Warna konsisten LLM vs SLM di seluruh repo
COLORS = {
    "llm": "#3b82f6",       # biru — LLM (hosted, "cloud")
    "slm_fp32": "#f59e0b",  # oranye — SLM full precision
    "slm_q4": "#10b981",    # hijau — SLM quantized
    "finetuned": "#8b5cf6", # ungu — fine-tuned model
    "neutral": "#6b7280",   # abu — baseline
}
