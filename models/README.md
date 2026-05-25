# models/

Tempat menyimpan **GGUF files** (TinyLlama Q4_K_M, dll) dan **fine-tuned checkpoints** dari modul 03.

File model **tidak di-commit** (gitignored — lihat `.gitignore`). Repo ini sengaja ringan; kamu re-download model dari HuggingFace / source aslinya.

## Struktur

```
models/
├── README.md           # file ini
├── .gitkeep            # supaya folder tetap ada di git
├── *.gguf              # quantized model (TinyLlama, dll) — gitignored
├── checkpoints/        # training checkpoint dari fine-tune — gitignored
└── finetuned/          # final fine-tuned model — gitignored
```

## HuggingFace cache

Model yang di-download via `transformers.AutoModel.from_pretrained(...)` di-cache di `~/.cache/huggingface/` by default, **bukan** di sini. Kalau kamu mau cache nya di dalam repo (lebih portable, tapi makan disk):

```bash
export HF_HOME="$(pwd)/models/hf_cache"
```

(Tambahkan ke `.env` atau `.bashrc` kamu.)

## Download GGUF (modul 02.03)

```python
from huggingface_hub import hf_hub_download

path = hf_hub_download(
    repo_id="TheBloke/TinyLlama-1.1B-Chat-v1.0-GGUF",
    filename="tinyllama-1.1b-chat-v1.0.Q4_K_M.gguf",
    local_dir="models/",
)
print(path)
```

Ukuran: ~670 MB.
