"""Download datasets used in this repo.

Run from repo root:
    python data/download_datasets.py

Downloads to data/cache/ (gitignored).

Datasets:
- IndoNLU SMSA (sentiment, 3 classes) — used in modul 03 & 04.01
- Liputan6 sample (summarization) — used in modul 04.02
"""
from __future__ import annotations

import sys
from pathlib import Path

CACHE_DIR = Path(__file__).resolve().parent / "cache"


def download_smsa() -> None:
    """IndoNLU SMSA sentiment dataset."""
    from datasets import load_dataset

    print("Downloading IndoNLU SMSA (sentiment)...")
    ds = load_dataset("indonlp/indonlu", "smsa", cache_dir=str(CACHE_DIR / "hf"))
    print(f"  train: {len(ds['train'])} samples")
    print(f"  validation: {len(ds['validation'])} samples")
    print(f"  test: {len(ds['test'])} samples")
    print(f"  labels: {ds['train'].features['label']}")


def download_liputan6_sample(n: int = 50) -> None:
    """Tiny Liputan6 sample for summarization experiments."""
    from datasets import load_dataset

    print(f"Downloading Liputan6 (first {n} samples for summarization)...")
    ds = load_dataset(
        "SEACrowd/liputan6_canonical",
        split=f"validation[:{n}]",
        cache_dir=str(CACHE_DIR / "hf"),
        trust_remote_code=True,
    )
    print(f"  loaded: {len(ds)} samples")
    sample = ds[0]
    keys = list(sample.keys())
    print(f"  keys: {keys}")


def main() -> int:
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    print(f"Cache dir: {CACHE_DIR}")

    try:
        download_smsa()
    except Exception as exc:
        print(f"[WARN] SMSA download gagal: {exc}", file=sys.stderr)

    try:
        download_liputan6_sample()
    except Exception as exc:
        print(f"[WARN] Liputan6 download gagal: {exc}", file=sys.stderr)

    print("\nSelesai. Dataset siap dipakai di notebook.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
