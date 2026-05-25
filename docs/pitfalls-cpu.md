# Pitfalls Khas CPU-Only

10 hal yang biasanya bikin pemula stuck saat eksperimen LLM/SLM di laptop tanpa GPU. Baca ini sebelum mulai.

---

## 1. `pip install torch` default narik wheel CUDA ~2GB

**Gejala**: download super lama, atau setelah install kamu lihat folder `~/.cache/pip` membengkak.

**Sebab**: PyPI default kasih wheel `torch+cu121` (CUDA). Padahal kita CPU-only.

**Solusi**: install torch **manual** dulu pakai index CPU:
```bash
pip install torch --index-url https://download.pytorch.org/whl/cpu
```
Baru lanjut `pip install -r requirements.txt`.

Verifikasi:
```python
import torch
assert not torch.cuda.is_available()  # ya, kita confirm DI MAU CPU
print(f"PyTorch {torch.__version__} (CPU)")
```

---

## 2. `llama-cpp-python` butuh build tools

**Gejala**: pip install error `error: Microsoft Visual C++ 14.0 is required` (Windows) atau `gcc not found` (Linux).

**Sebab**: `llama-cpp-python` compile dari source kalau wheel pre-built untuk Python version mu tidak ada.

**Solusi (Linux/WSL)**:
```bash
sudo apt-get update && sudo apt-get install -y build-essential cmake
```

**Solusi (Mac)**: `xcode-select --install`.

**Solusi (Windows)**: install Visual Studio Build Tools, atau lebih mudah pakai WSL.

**Fallback kalau benar-benar tidak bisa install**: skip notebook 02.03 (quantization). Materi lain tetap jalan.

---

## 3. HuggingFace cache makan disk diam-diam

**Gejala**: tiba-tiba disk penuh, `~/.cache/huggingface` jadi 5GB.

**Sebab**: Setiap `from_pretrained()` download model + tokenizer + config. Tidak otomatis dibersihkan.

**Cek isi cache**:
```bash
huggingface-cli scan-cache
```

**Hapus model yang tidak dipakai**:
```bash
huggingface-cli delete-cache
```

**Pindah cache ke disk lain** (misalnya HDD eksternal):
```bash
export HF_HOME=/path/to/big/disk/huggingface
```
Tambahkan ke `.bashrc` atau `.env` repo ini.

---

## 4. Model >1B di fp32 = OOM di laptop 8GB RAM

**Gejala**: kernel crash, OS swap berat, "MemoryError" saat `from_pretrained()`.

**Hard rule untuk repo ini**:
- ≤ 200M params → boleh fp32 lewat `transformers` (DistilBERT, SmolLM2-135M).
- > 200M params → **wajib** quantized GGUF lewat `llama-cpp-python` (TinyLlama Q4, dst).
- > 3B params → tidak realistis di CPU laptop. Pakai API (Groq).

Kalau RAM mu < 16GB, skip notebook 02.03 dan jalankan TinyLlama lewat API saja.

---

## 5. Groq 401 / call hang

**Gejala**: `openai.AuthenticationError: 401`, atau call diam tanpa response.

**Penyebab umum**:
- Lupa `cp .env.example .env`.
- `.env` ada tapi `GROQ_API_KEY=` (kosong setelah `=`).
- Lupa `from dotenv import load_dotenv; load_dotenv()` di notebook.

**Cara cepat verify**:
```python
import os
from dotenv import load_dotenv
load_dotenv()
key = os.getenv("GROQ_API_KEY")
assert key, "GROQ_API_KEY belum di-set. Cek .env"
print(f"Key OK ({len(key)} chars)")
```

**Daftar gratis (no credit card)**: https://console.groq.com/keys

---

## 6. Tokenizer download timeout di ISP Indonesia

**Gejala**: `transformers` macet di "Downloading tokenizer.json", error TimeoutError, atau speed < 100 KB/s.

**Solusi 1**: pasang `hf_transfer` (download paralel chunk):
```bash
pip install hf_transfer
export HF_HUB_ENABLE_HF_TRANSFER=1
```

**Solusi 2**: pakai mirror (kalau hf.co di-throttle ISP mu):
```bash
export HF_ENDPOINT=https://hf-mirror.com
```

Ini real issue untuk beberapa ISP Indonesia. Tidak harus dipakai semua orang.

---

## 7. Re-run cell load model = duplikat di RAM

**Gejala**: sebelumnya jalan, sekarang OOM. Padahal kode tidak berubah.

**Sebab**: cell `model = AutoModel.from_pretrained(...)` di-run ulang. Object lama belum di-garbage-collect, sekarang ada dua copy di RAM.

**Solusi (di awal cell load model)**:
```python
import gc
try:
    del model
    del tokenizer
except NameError:
    pass
gc.collect()

# baru load model
```

**Solusi paling aman antar notebook besar**: restart kernel (Kernel → Restart) sebelum notebook baru.

---

## 8. Benchmark angka noisy

**Gejala**: jalan benchmark dua kali, hasil beda 30%.

**Sebab**: thermal throttling, browser di background, GC pause, swap.

**Protokol benchmark di repo ini**:
- 3x run, ambil **median** (bukan mean — outlier mengkacaukan mean).
- Tutup browser dan app berat sebelum run.
- Plug ke listrik, bukan baterai (laptop sering throttle CPU di baterai).
- Jangan freak out kalau angka absolut beda dari laptop teman. **Yang penting RATIO** antar model di mesin yang sama.

---

## 9. Bahasa Indonesia fragments di tokenizer English-trained

**Gejala**: prompt 10 kata Bahasa = 18 token, prompt 10 kata English = 12 token. Biaya API & latency lebih tinggi untuk Bahasa.

**Sebab**: tokenizer (BPE) pre-trained dominan corpus English. Kata Bahasa yang tidak muncul di corpus English di-pecah jadi sub-token panjang.

**Implikasi**:
- Prompt Bahasa 1.5–2x lebih mahal di API daripada English equivalent.
- Context window terasa lebih sempit untuk Bahasa.
- SLM lokal yang generate Bahasa sering kurang fluent dibanding English.

Pelajaran ini di-surface eksplisit di notebook 02.01 — jangan kaget.

---

## 10. nanoGPT-style training "stuck" 30 detik pertama

> Tidak relevan di repo ini (from-scratch transformer di-skip, lihat `llm-internals` repo).

Tapi prinsip terkait yang relevan untuk **fine-tune notebook (modul 03)**:

**Gejala**: training cell jalan, tapi tidak ada output 1 menit pertama.

**Sebab**: log per-epoch baru muncul di akhir epoch. Kalau 1 epoch butuh 5 menit, kamu nungguin 5 menit sebelum tahu apakah training jalan.

**Solusi**: pakai callback yang log per-step (mis. `logging_steps=50` di `TrainingArguments`). Notebook 03.01 set ini secara default.

---

## Kalau masih stuck

Kalau pesan error tidak ada di sini, copy ke catatan terpisah:
1. Pesan error lengkap.
2. Notebook & cell mana.
3. Output `pip list | grep -E "torch|transformers|llama-cpp"`.
4. Output `python --version` dan OS.

Ini cukup untuk debug 90% kasus.
