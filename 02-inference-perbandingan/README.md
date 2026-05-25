# 02 — Inference: Perbandingan LLM vs SLM

Modul paling "wow" di repo ini. Kita panggil LLM lewat API (Groq) dan SLM lokal di laptop kamu, lalu bandingkan langsung: latency, RAM, kualitas output, biaya per 1000 token.

## Notebook

| # | File | Topik |
|---|---|---|
| 02.01 | [01_hello_groq_llm.ipynb](01_hello_groq_llm.ipynb) | First call ke Groq, streaming, hitung token & biaya |
| 02.02 | [02_hello_local_slm.ipynb](02_hello_local_slm.ipynb) | Load SmolLM2-135M dengan `transformers`, generate teks |
| 02.03 | [03_quantization_dengan_llamacpp.ipynb](03_quantization_dengan_llamacpp.ipynb) | TinyLlama-1.1B Q4 GGUF — apa itu quantization, kenapa lebih cepat |
| 02.04 | [04_benchmark_side_by_side.ipynb](04_benchmark_side_by_side.ipynb) | 10 prompt sama → tabel perbandingan latency, RAM, biaya, kualitas |

## Prasyarat

- Modul 00 lulus (env siap, API key set).
- Modul 01 sudah dibaca (paham apa itu LLM/SLM).

## Apa yang bikin modul ini berkesan

Pertama kali kamu lihat **Llama-3.1-8B di Groq jawab dalam 300ms** sementara **SmolLM2-135M di laptop kamu butuh 8 detik**, otomatis ngerasa: "oh, jadi ini bedanya". Yang penting bukan angka mutlaknya — tapi *ratio* nya, dan kapan ratio itu masuk akal.

## Cross-link

- Internals quantization (apa yang sebenarnya terjadi di Q4_K_M)? → [`llm-internals`](../../llm-internals/) modul 05.
