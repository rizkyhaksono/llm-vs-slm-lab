# Referensi

Sumber materi yang dipakai / direkomendasikan untuk pendalaman.

---

## Repo Pelengkap (di workspace yang sama)

- **[`hands-on-classic-ml`](../../hands-on-classic-ml/)** — fondasi classical ML (linear regression, tree, gradient descent). Wajib paham sebelum lanjut ke deep learning.
- **[`neural-from-scratch`](../../neural-from-scratch/)** — bangun NN dari nol gaya Karpathy: autograd, MLP, CNN, RNN, dan Transformer mini-GPT (modul 05).
- **[`llm-internals`](../../llm-internals/)** — internals NLP & LLM secara mendalam: tokenization, attention, transformer from scratch, fine-tuning + LoRA + PEFT + quantization.

> Repo ini (`llm-vs-slm-lab`) fokus comparison & praktek. Untuk paham *mekanisme di dalam*, lihat tiga repo di atas.

---

## Model & Library

- **HuggingFace Transformers** — https://huggingface.co/docs/transformers
- **HuggingFace Datasets** — https://huggingface.co/docs/datasets
- **SmolLM2** model card — https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct
- **TinyLlama** model card — https://huggingface.co/TinyLlama/TinyLlama-1.1B-Chat-v1.0
- **DistilBERT** paper — https://arxiv.org/abs/1910.01108
- **llama.cpp** — https://github.com/ggerganov/llama.cpp

---

## API Provider

- **Groq Console** (free tier) — https://console.groq.com
- **OpenRouter** (fallback, banyak model) — https://openrouter.ai

---

## Dataset Bahasa Indonesia

- **IndoNLU** — benchmark NLP Bahasa: https://github.com/IndoNLP/indonlu
- **NusaCrowd / SEACrowd** — kumpulan dataset Bahasa Indonesia dan Asia Tenggara: https://github.com/SEACrowd
- **Liputan6 dataset** (summarization) — https://huggingface.co/datasets/SEACrowd/liputan6_canonical

---

## Bacaan / Video Konseptual

- **Andrej Karpathy — "Intro to Large Language Models"** (1 jam, YouTube) — gambaran besar yang sangat clear: https://www.youtube.com/watch?v=zjkBMFhNj_g
- **Karpathy — "Let's build GPT from scratch"** (untuk yang mau internals): https://www.youtube.com/watch?v=kCc8FmEb1nY
- **HuggingFace SmolLM blog** — kenapa SLM kecil bisa kompetitif: https://huggingface.co/blog/smollm

---

## Paper Penting (kalau mau dalam)

- **"Attention is All You Need"** (Vaswani et al., 2017) — original Transformer.
- **"Scaling Laws for Neural Language Models"** (Kaplan et al., 2020) — kenapa "lebih besar lebih baik", dan kapan plateau.
- **"Training Compute-Optimal Large Language Models"** (Hoffmann et al., 2022 — Chinchilla) — koreksi Kaplan: data scaling lebih penting dari yang dikira.
- **"Phi-3 Technical Report"** (Microsoft, 2024) — argumen kuat untuk SLM: data quality > size.
- **"LoRA: Low-Rank Adaptation of Large Language Models"** (Hu et al., 2021).

---

## Cheatsheet & Cookbook

- **HuggingFace Cookbook** — https://huggingface.co/learn/cookbook
- **OpenAI Cookbook** (banyak pattern reusable, OpenAI-compatible client → bisa pakai untuk Groq juga) — https://cookbook.openai.com
