# 04 — Case Study: LLM vs SLM Head-to-Head

Setelah paham konsep, sudah benchmark inference, dan sudah fine-tune satu model — sekarang kita aplikasikan ke task konkret. Setiap notebook = satu skenario aplikasi nyata, dengan kesimpulan yang opinionated.

## Notebook

| # | File | Topik |
|---|---|---|
| 04.01 | [01_classification_distilbert_vs_groq.ipynb](01_classification_distilbert_vs_groq.ipynb) | Sentiment SMSA: DistilBERT (fine-tuned) vs Llama-3.1 few-shot — accuracy, latency, biaya, kompleksitas operasional |
| 04.02 | [02_summarization_groq_vs_tinyllama.ipynb](02_summarization_groq_vs_tinyllama.ipynb) | 5 artikel Liputan6: Groq vs TinyLlama Q4 |
| 04.03 | [03_qa_dengan_konteks_mini_rag.ipynb](03_qa_dengan_konteks_mini_rag.ipynb) | Mini RAG: retrieve chunk → jawab dengan Groq, vs DistilBERT-QA lokal |

## Prasyarat

- Modul 03 lulus (sudah pernah fine-tune DistilBERT).

## Apa yang bikin case study di sini berbeda?

Banyak tutorial benchmark cuma kasih angka. Notebook di sini menambahkan kolom yang sering dilupakan:

- **Biaya operasional** — bukan cuma $/1k token API, tapi juga "berapa lama tim mu butuh untuk maintain ini".
- **Privacy & data residency** — kalau data sensitive, API langsung tertutup.
- **Skenario pengguna** — siapa user nya, latency budget berapa, bisa toleransi error berapa banyak.
