# data/

Dataset tidak di-commit (bisa besar dan license nya bukan punya kita). Pakai `download_datasets.py` untuk ambil dataset yang dipakai di repo ini.

## Cara pakai

```bash
# dari root repo
python data/download_datasets.py
```

Script akan download:

- **IndoNLU SMSA** — sentiment Bahasa Indonesia, 3 kelas (positif/netral/negatif). Dipakai di modul 03 (fine-tuning) dan 04 (case study klasifikasi).
- **Liputan6 sample** — 50 artikel berita Bahasa untuk test summarization. Dipakai di modul 04.

Output disimpan di `data/cache/` (gitignored).

## Sumber

- IndoNLU: https://github.com/IndoNLP/indonlu (Apache-2.0)
- Liputan6: https://huggingface.co/datasets/SEACrowd/liputan6_canonical
