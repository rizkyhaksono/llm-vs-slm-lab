# 03 — Fine-Tuning Praktis

Kita ambil model encoder kecil (DistilBERT 66M params), terus lanjutkan training nya di dataset sentiment Bahasa Indonesia. Tujuannya bukan jadi expert fine-tuning — tujuannya merasakan workflow end-to-end di CPU.

## Notebook

| # | File | Topik |
|---|---|---|
| 03.01 | [01_finetune_distilbert_smsa.ipynb](01_finetune_distilbert_smsa.ipynb) | Full fine-tune DistilBERT di IndoNLU SMSA (sentiment) — 3 epoch, ~15–25 menit di CPU |

## Prasyarat

- Modul 02 lulus (paham loading model, sudah pernah inference).

## Kenapa DistilBERT, bukan SmolLM2?

Encoder model (BERT family) jauh lebih kecil dan ringan untuk klasifikasi dibanding generative model. 66M params, full fine-tune di CPU realistis. SmolLM2-135M sudah generative jadi training nya butuh dataset jauh lebih besar dan lebih lambat.

## Kenapa tidak pakai LoRA?

LoRA solving "GPU ku tidak muat 7B model". Pada model 66M di CPU, LoRA solving non-problem — full fine-tune malah lebih sederhana dan cukup cepat.

Kalau kamu mau LoRA / PEFT secara mendalam → lanjut ke [`llm-internals`](../../llm-internals/) modul 05.
