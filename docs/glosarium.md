# Glosarium LLM & SLM

Definisi singkat istilah yang sering muncul. Format: **Istilah (English)** — penjelasan 1–3 kalimat.

> Untuk istilah classical ML (loss, gradient, overfitting, dll), lihat [`hands-on-classic-ml/docs/glosarium.md`](../../hands-on-classic-ml/docs/glosarium.md).

---

## A

**Attention** — Mekanisme inti transformer: setiap token "melihat" ke semua token sebelumnya dan memberi bobot relevansi. Hasilnya context-aware embedding. Detail di [`llm-internals/03`](../../llm-internals/).

**Autoregressive** — Cara generate teks: prediksi token berikutnya berdasarkan semua token sebelumnya, lalu append, ulang. GPT-family begini.

## B

**Base model** — Model setelah pre-training, sebelum instruction tuning. Bisa "lanjutkan teks" tapi belum tentu jawab pertanyaan. Lawan: instruct-tuned.

**Batch size** — Berapa contoh diproses sekaligus dalam satu forward/backward pass. Di CPU, batch kecil (8–16) realistis.

**BPE (Byte Pair Encoding)** — Algoritma tokenizer paling umum sekarang. Pecah teks jadi sub-word. Detail di [`llm-internals/01`](../../llm-internals/).

## C

**Context window** — Maksimal token yang bisa diingat model dalam satu call. Llama-3.1-8B = 128k, SmolLM2 = 8k. Makin besar, makin haus memory.

**Cost per 1k tokens** — Satuan harga API. Groq llama-3.1-8b-instant ≈ $0.05/1k input, $0.08/1k output (Mei 2026, cek harga terkini).

## D

**DistilBERT** — Versi lebih kecil dari BERT (66M params). Encoder-only, cocok untuk klasifikasi. Dipakai di modul 03.

## E

**Embedding** — Representasi vektor (biasanya 256–4096 dimensi) dari token / kata / kalimat. Token dengan makna mirip → vektor berdekatan.

**Encoder-only** — Arsitektur seperti BERT. Bagus untuk understanding tasks (klasifikasi, NER, QA ekstraktif). Tidak generate teks.

## F

**Fine-tuning** — Lanjutkan training model pre-trained di dataset spesifik task mu. Dua varian besar: full fine-tune (semua param trainable) vs PEFT/LoRA (sebagian kecil).

**Few-shot prompting** — Kasih 2–5 contoh di prompt sebelum tanya. LLM API biasanya cukup hebat dengan few-shot tanpa fine-tune.

## G

**GGUF** — Format file model quantized untuk `llama.cpp`. Self-contained: weights + tokenizer + config dalam 1 file. Standar untuk inference CPU.

**Greedy decoding** — Generate selalu pilih token paling probable. Output deterministik tapi sering monoton. Lawan: sampling (top-k, top-p, temperature).

**Groq** — Provider API LLM yang cepat (LPU hardware). Free tier-nya generous. Dipakai di repo ini sebagai LLM utama.

## H

**HuggingFace Hub** — Repository utama model open-weight + dataset. `transformers` library default-nya download dari sini.

## I

**Instruct-tuned** — Base model yang sudah di-fine-tune di dataset berformat (instruction → response). Bisa "menjawab", bukan cuma "melanjutkan teks".

**Inference** — Pakai model untuk prediksi (tidak training). Inference LLM = generate output untuk input baru.

## L

**Latency** — Waktu dari kirim request sampai dapat response (atau token pertama). Groq: ~300ms. SmolLM2 di CPU: ~5–10 detik.

**llama.cpp** — Engine C++ untuk inference LLM di CPU (atau GPU). Standar di-facto untuk model quantized di mesin terbatas. `llama-cpp-python` adalah binding nya.

**LoRA (Low-Rank Adaptation)** — Teknik fine-tuning yang freeze model utama, train matrix kecil tambahan. Hemat memory. Detail di [`llm-internals/05`](../../llm-internals/).

**LLM (Large Language Model)** — Generative language model dengan miliaran (1B–500B+) params. Contoh: GPT-4, Llama-3.1-8B/70B/405B, Claude Opus. Repo ini akses via API.

## M

**Multi-head attention** — Beberapa attention heads paralel, masing-masing belajar relasi berbeda. Detail di [`llm-internals/03`](../../llm-internals/).

## P

**Parameters** — Jumlah weight trainable di model. SmolLM2 = 135M, Llama-3.1 = 8B = 8 × 10⁹.

**PEFT (Parameter-Efficient Fine-Tuning)** — Family teknik fine-tune cuma sebagian param: LoRA, QLoRA, prefix-tuning, dll.

**Pre-training** — Training awal di corpus besar (trillion tokens) dengan objective umum (next-token prediction). Mahal banget; biasanya kita pakai hasilnya.

**Prompt** — Input ke language model. Bisa system prompt + user message + assistant message (chat) atau plain text (completion).

## Q

**Quantization** — Kompres weight model dari fp32 (32-bit) ke int8 / int4 / int2. Tradeoff: ukuran/kecepatan vs kualitas. Q4_K_M = good balance, dipakai di repo ini.

## R

**RAG (Retrieval Augmented Generation)** — Teknik: retrieve dokumen relevan dulu, baru append ke prompt → model jawab dengan konteks. Bantu LLM jawab tentang data yang tidak ada di training.

## S

**Sampling temperature** — Parameter generate: 0 = deterministik (greedy), 1 = balanced, >1 = lebih kreatif/acak.

**SLM (Small Language Model)** — Tidak ada threshold formal, tapi consensus longgar: < 7B params. Beberapa orang pakai < 1B sebagai cutoff. Definisi praktis: model yang **muat di mesin biasa**.

**SmolLM2** — Family model kecil dari HuggingFace (135M, 360M, 1.7B). Dipakai di repo ini sebagai SLM contoh.

**Streaming** — API mengirim token satu per satu (Server-Sent Events) saat di-generate, bukan tunggu lengkap. UX lebih baik (mulai baca cepat).

## T

**Token** — Unit terkecil yang dilihat model. Bukan "kata" — bisa sub-kata, simbol, byte. Bahasa English: ~0.75 kata/token. Bahasa Indonesia: ~0.5 kata/token (boros).

**Tokenizer** — Komponen yang convert text ↔ token IDs. Pre-trained dengan model nya.

**Top-k / Top-p (nucleus)** — Sampling strategy: top-k pilih dari k token paling probable, top-p pilih dari sebanyak token sampai cumulative prob ≥ p.

**Training data scale** — LLM modern: trillion tokens. SLM kecil: hundred billion. Skala data **lebih menentukan kualitas dari ukuran model**, sampai titik tertentu.

## V

**vLLM, TGI** — Engine inference LLM untuk production (GPU). Tidak relevan di repo ini (kita CPU).

## Z

**Zero-shot** — Tanya tanpa contoh sama sekali. LLM modern jago zero-shot; SLM kecil sering perlu few-shot.
