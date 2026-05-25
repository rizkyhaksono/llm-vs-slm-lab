"""Helper utilities untuk notebook di repo ini.

Submodule (import sesuai kebutuhan, JANGAN eager import semua di sini supaya
notebook yang cuma butuh plotting tidak ikut narik dependency openai/llama-cpp):

- utils.benchmark    : latency, RAM, token counting
- utils.llm_clients  : factory client Groq / OpenRouter + get_secret()
- utils.plotting     : matplotlib styling konsisten

Contoh:
    from utils.plotting import setup_style          # cuma butuh matplotlib
    from utils.llm_clients import groq_client        # baru narik openai di sini
"""

__all__ = ["benchmark", "llm_clients", "plotting"]
