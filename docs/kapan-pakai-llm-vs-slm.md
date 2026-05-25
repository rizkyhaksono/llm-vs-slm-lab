# Cheatsheet: Kapan Pakai LLM, Kapan Pakai SLM?

Decision framework cepat. Companion untuk modul 05.

> Aturan emas: **default ke yang paling sederhana yang berhasil**. LLM API biasanya simplest start. SLM lokal dipakai saat ada alasan konkret.

---

## Pertanyaan untuk Dijawab Dulu

Sebelum pilih, kamu perlu tahu jawaban dari 5 pertanyaan ini:

1. **Latency budget**: berapa ms response time max yang user toleransi?
2. **Privacy**: apakah data user/pasien/finansial yang tidak boleh keluar dari server kamu?
3. **Volume & biaya**: berapa request per hari? di scale itu, mana yang lebih murah?
4. **Domain spesifik**: apakah kamu punya data labeled spesifik yang bisa bikin model kecil mengalahkan LLM general?
5. **Kompleksitas tim**: tim kamu bisa maintain MLOps untuk model lokal? atau lebih nyaman pakai API?

---

## Decision Tree (Versi Cepat)

```
Pertanyaan 1: Apakah data sensitive (PII, kesehatan, finansial)?
├── Ya  → SLM lokal / fine-tuned (privacy hard requirement)
└── Tidak → lanjut

Pertanyaan 2: Apakah task butuh reasoning kompleks / multi-step?
                 (math word problem, coding non-trivial, planning)
├── Ya  → LLM API (SLM kecil tidak akan cukup)
└── Tidak → lanjut

Pertanyaan 3: Apakah task = klasifikasi / extraction / structured output sederhana?
├── Ya  → SLM (DistilBERT fine-tuned biasanya menang akurasi & jauh lebih murah)
└── Tidak → lanjut

Pertanyaan 4: Volume request > 10k/hari?
├── Ya  → Hitung biaya. LLM API di volume itu sering > $200/bulan;
│         SLM lokal sering lebih murah kalau sudah punya server.
└── Tidak → LLM API (start simple, optimize later)

Pertanyaan 5: Latency budget < 500ms p95?
├── Ya  → Groq atau SLM lokal. Bukan OpenAI/Anthropic API (sering 1–3s).
└── Tidak → LLM API standar OK.
```

---

## Tabel Ringkas

| Skenario | Pilihan default | Alasan |
|---|---|---|
| Chatbot customer service general | **LLM API (Groq / Anthropic / OpenAI)** | Quality bar tinggi, low effort start |
| Sentiment analysis 10k komentar / hari | **SLM fine-tuned (DistilBERT)** | Klasifikasi sederhana, biaya 1/100 LLM, lebih cepat |
| Summarization artikel berita | **LLM API** kalau quality penting; **SLM Q4** kalau on-device | LLM lebih natural; SLM cukup kalau privacy/offline |
| Extraksi entitas (NER) dari dokumen | **SLM fine-tuned** | NER classical sangat efisien dengan encoder model |
| Coding assistant / agent kompleks | **LLM API (besar)** | SLM kecil tidak punya world knowledge cukup |
| QA atas dokumentasi internal (private) | **SLM lokal + RAG** atau **LLM API + RAG** dengan privacy contract | Tergantung kontrak privacy & ukuran corpus |
| App mobile yang harus offline | **SLM Q4** (TinyLlama / Phi-3-mini Q4) | Tidak ada pilihan lain |
| Prototype cepat untuk demo | **LLM API** | Speed-to-demo > optimisasi |

---

## Kesalahan Klasik

1. **"Kita pakai LLM untuk sentiment analysis"** — sering 100x overkill. DistilBERT fine-tuned lebih akurat di domain mu, jauh lebih murah, lebih cepat.
2. **"Kita self-host Llama-70B"** — kecuali tim kamu MLOps-ready dengan GPU cluster, biaya engineering > harga API setahun.
3. **"SLM lokal pasti lebih privat"** — benar **kalau** kamu juga jaga: log, network egress, dependencies. Cuma jalankan model lokal tanpa hardening tidak otomatis aman.
4. **"Quantization gratis"** — Q4 kadang turun kualitas signifikan untuk task delicate (math, code). Selalu A/B test.
5. **"Lebih kecil = lebih hemat"** — biaya inference bukan satu-satunya cost. Maintenance, model updating, monitoring juga ada.

---

## Hybrid Pattern

Banyak production system pakai *kombinasi*:

- **Routing**: SLM cepat klasifikasi intent → LLM mahal cuma dipanggil untuk kasus kompleks.
- **Cascade**: SLM coba dulu, kalau confidence rendah eskalasi ke LLM.
- **Distill**: pakai LLM bagus untuk generate dataset, fine-tune SLM dengan dataset itu — production pakai SLM.

---

## Update di 2026

Reality check: garis LLM/SLM bergerak terus. Mei 2026:
- **Llama-3.3-8B** (di Groq, gratis): kualitas mendekati GPT-4 turbo 2024.
- **Phi-3-mini-4k (3.8B Q4)**: ~bisa dijalankan di laptop modern, kualitas dasar untuk banyak task.
- **SmolLM2-1.7B**: smallest yang masih masuk kategori "useful chat" untuk tugas ringan.

Cek lagi kalau kamu baca ini setelah 2027 — pasti udah berubah. Tapi pertanyaan-pertanyaan di atas **tidak berubah**.
