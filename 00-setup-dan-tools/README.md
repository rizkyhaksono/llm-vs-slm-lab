# 00 — Setup & Tools

Verifikasi environment kerja siap. Kalau notebook di sini lulus semua, kamu boleh lanjut ke modul 01.

## Notebook

| # | File | Topik |
|---|---|---|
| 00.01 | [01_setup_environment.ipynb](01_setup_environment.ipynb) | Cek Python, torch CPU, HuggingFace, Groq API key, sample model |

## Yang harus disiapkan dulu

1. Python 3.10+
2. Sudah `python -m venv .venv && source .venv/bin/activate`
3. Sudah `pip install torch --index-url https://download.pytorch.org/whl/cpu`
4. Sudah `pip install -r requirements.txt`
5. Sudah `cp .env.example .env` dan isi `GROQ_API_KEY` (gratis di https://console.groq.com)

Kalau ada yang macet, baca [docs/pitfalls-cpu.md](../docs/pitfalls-cpu.md) — biasanya jawabannya ada di sana.
