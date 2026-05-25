# LLM vs SLM Lab

Jurnal belajar membedakan **Large Language Model (LLM)** vs **Small Language Model (SLM)** — fokus ke perbandingan praktis: kapan pakai yang mana, biaya & latency, fine-tuning ringan, dan studi kasus konkret.

> Target pembaca: software engineer / AI engineer yang sudah bisa Python tapi belum pernah pegang LLM/SLM lebih dari sekadar pakai ChatGPT. Hardware **CPU-only** — tidak butuh GPU.

---

## Filosofi Repo Ini

1. **Fokus comparison, bukan internals.** Repo ini menjawab pertanyaan praktis "kapan pakai LLM, kapan SLM?" — bukan "bagaimana attention bekerja di level matriks". Untuk internals, lihat repo pelengkap di bawah.
2. **Realistis di CPU.** Setiap eksperimen dirancang berjalan <30 menit di laptop biasa. Tidak ada model 7B fp32, tidak ada training dari nol berhari-hari.
3. **Bandingkan apple-to-apple.** Setiap notebook benchmark menjalankan prompt/task yang sama di LLM (hosted API) dan SLM (lokal), lalu hasilnya ditabulasi: latency, RAM, biaya, kualitas.
4. **Bahasa narasi: Indonesia.** Istilah teknis tetap English (`tokenizer`, `quantization`, `latency`) supaya nyambung saat baca paper / dokumentasi.
5. **Reproducible.** Setiap notebook punya seed tetap dan output yang bisa dibandingkan ulang.

---

## Cara Pakai Repo Ini

### 1. Setup environment

```bash
# clone (kalau dari github)
git clone <repo-url> llm-vs-slm-lab
cd llm-vs-slm-lab

# bikin venv (sangat disarankan biar tidak bentrok dengan project lain)
python -m venv .venv
source .venv/bin/activate     # Linux / WSL / Mac
# .venv\Scripts\activate       # Windows PowerShell

# WAJIB: install torch CPU-only DULU (sebelum requirements.txt)
# Default `pip install torch` akan narik wheel CUDA ~2GB yang tidak dipakai.
pip install torch --index-url https://download.pytorch.org/whl/cpu

# install sisanya
pip install -r requirements.txt

# daftarkan kernel ke Jupyter
python -m ipykernel install --user --name=llm-vs-slm-lab --display-name="Python (llm-vs-slm-lab)"

# isi API key
cp .env.example .env
# edit .env, masukkan GROQ_API_KEY (gratis di https://console.groq.com)

# jalankan
jupyter lab
# atau buka langsung di VSCode → pilih kernel "llm-vs-slm-lab"
```

> Lihat [docs/pitfalls-cpu.md](docs/pitfalls-cpu.md) sebelum mulai. Ada 10 hal khas CPU-only yang sering bikin pemula stuck.

### 1b. Alternatif: jalan di Google Colab

Tidak punya laptop yang kuat? Jalankan di Colab (gratis). Bedanya: **file `.env` tidak ikut** saat clone (sengaja — di-gitignore), jadi API key di-set lewat **Colab Secrets**, bukan `.env`.

1. Buka [colab.research.google.com](https://colab.research.google.com) → upload / buka notebook dari repo ini.
2. Set API key: klik ikon **kunci 🔑** di sidebar kiri → **Add new secret** → Name: `GROQ_API_KEY`, Value: key kamu → aktifkan **Notebook access**.
3. Cell pertama tiap notebook (section 0 "Bootstrap") otomatis clone repo + install dependencies + set path. Ganti `REPO_URL` di cell itu dengan URL GitHub repo kamu.

Helper `get_secret()` di [utils/llm_clients.py](utils/llm_clients.py) otomatis baca dari Colab Secrets (kalau di Colab) atau `.env` (kalau lokal) — jadi **kode notebook nya sama persis** di dua environment.

### 2. Urutan belajar

| Folder | Topik | Estimasi |
|---|---|---|
| [00-setup-dan-tools/](00-setup-dan-tools/) | Verifikasi environment, API key, sample model | 30–45 menit |
| [01-konsep-llm-vs-slm/](01-konsep-llm-vs-slm/) | Apa itu language model, definisi LLM vs SLM | 1–2 jam |
| [02-inference-perbandingan/](02-inference-perbandingan/) | Hello Groq, hello SmolLM2, quantization GGUF, benchmark side-by-side | 3–4 jam |
| [03-finetuning-praktis/](03-finetuning-praktis/) | Fine-tune DistilBERT untuk sentiment Bahasa | 2–3 jam |
| [04-case-study/](04-case-study/) | Klasifikasi, summarization, QA — LLM vs SLM head-to-head | 3–5 jam |
| [05-kapan-pakai-apa/](05-kapan-pakai-apa/) | Decision framework + mini project | 2–3 jam |

**Total: 2–3 weekend santai.**

### 3. Cara baca notebook

Tiap notebook punya struktur konsisten:

1. **Tujuan & Konteks** — apa yang akan kamu pelajari dan kenapa
2. **Prasyarat** — notebook / konsep yang harus sudah kamu lewati
3. **Konsep & Intuisi** — penjelasan singkat (bukan textbook)
4. **Hands-on / Eksperimen** — kode yang dijalankan, dengan output sample
5. **Refleksi & Insight** — apa yang menarik dari hasil
6. **Latihan Mandiri** — 1–2 soal opsional
7. **Cross-link** — ke notebook lain / repo lain kalau mau lebih dalam

---

## Struktur Repo

```
llm-vs-slm-lab/
├── 00-setup-dan-tools/           # Verifikasi environment + API key
├── 01-konsep-llm-vs-slm/         # Definisi & intuisi (no code berat)
├── 02-inference-perbandingan/    # LLM (Groq) vs SLM (lokal) side-by-side
├── 03-finetuning-praktis/        # Fine-tune DistilBERT
├── 04-case-study/                # Klasifikasi, summarization, QA
├── 05-kapan-pakai-apa/           # Decision framework + mini project
├── data/                         # Download script (dataset tidak di-commit)
├── models/                       # Tempat GGUF; HF cache di ~/.cache
├── utils/                        # benchmark, llm_clients, plotting helpers
└── docs/                         # Glosarium, pitfalls, referensi, cheatsheet
```

---

## Repo Pelengkap

Repo ini **tidak menjelaskan internals secara mendalam**. Kalau kamu mau paham mekanisme di dalam transformer (attention, embedding, dari nol), lanjut ke:

- **[`neural-from-scratch`](../neural-from-scratch/)** — bangun NN dari nol gaya Karpathy. Modul 05 nya khusus Transformer / mini-GPT.
- **[`llm-internals`](../llm-internals/)** — NLP & LLM internals mendalam. Modul 01 (tokenization), 03 (attention), 04 (transformer from scratch), 05 (fine-tuning + LoRA + PEFT + quantization).

Repo ini fokus ke **pertanyaan praktis level senior**: kapan pilih LLM, kapan SLM, kenapa, dengan data konkret.

---

## Status Progress

- [x] Setup repo & struktur folder
- [ ] `00-setup-dan-tools/01_setup_environment.ipynb`
- [ ] `01-konsep-llm-vs-slm/01_apa_itu_language_model.ipynb`
- [ ] `01-konsep-llm-vs-slm/02_llm_vs_slm_definisi.ipynb`
- [ ] `02-inference-perbandingan/*` (4 notebook)
- [ ] `03-finetuning-praktis/01_finetune_distilbert_smsa.ipynb`
- [ ] `04-case-study/*` (3 notebook)
- [ ] `05-kapan-pakai-apa/*` (2 notebook)

---

## Referensi Utama

- **HuggingFace Transformers docs** — sumber utama untuk model loading & inference: https://huggingface.co/docs/transformers
- **SmolLM2 model card** — https://huggingface.co/HuggingFaceTB/SmolLM2-135M-Instruct
- **llama.cpp** — engine quantization & CPU inference: https://github.com/ggerganov/llama.cpp
- **Groq Console** — free tier API: https://console.groq.com
- **IndoNLU** — benchmark NLP Bahasa Indonesia: https://github.com/IndoNLP/indonlu

Lengkapnya di [docs/referensi.md](docs/referensi.md).

---

## Lisensi

Repo ini untuk pembelajaran personal. Silakan fork & ikut belajar.
