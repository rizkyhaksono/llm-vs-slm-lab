"""Factory client untuk LLM API.

Groq dan OpenRouter dua-duanya OpenAI-compatible — cuma beda base_url dan
key env var. Kita pakai openai SDK untuk dua-duanya.

Usage:
    from utils.llm_clients import groq_client

    client = groq_client()
    resp = client.chat.completions.create(
        model="llama-3.1-8b-instant",
        messages=[{"role": "user", "content": "Halo!"}],
    )
    print(resp.choices[0].message.content)
"""
from __future__ import annotations

import os

from dotenv import load_dotenv
from openai import OpenAI

# auto-load .env saat module di-import (idempotent)
load_dotenv()

GROQ_BASE_URL = "https://api.groq.com/openai/v1"
OPENROUTER_BASE_URL = "https://openrouter.ai/api/v1"


def get_secret(name: str) -> str | None:
    """Ambil secret dari sumber yang tepat tergantung environment.

    Urutan cek:
    1. Google Colab Secrets (ikon kunci di sidebar) — kalau jalan di Colab.
    2. Environment variable / .env file — kalau jalan lokal.

    Notebook yang sama jadi jalan di lokal maupun Colab tanpa ganti kode.
    """
    # 1. Google Colab Secrets
    try:
        from google.colab import userdata  # type: ignore

        try:
            val = userdata.get(name)
            if val:
                return val
        except Exception:
            # SecretNotFoundError / NotebookAccessError → lanjut ke fallback
            pass
    except ImportError:
        pass  # bukan di Colab, normal

    # 2. Lokal: environment variable (sudah di-load dari .env di atas)
    return os.getenv(name)


def _missing_key_error(env_name: str, signup_url: str) -> RuntimeError:
    return RuntimeError(
        f"{env_name} belum di-set.\n"
        "Kalau di LOKAL:\n"
        "  - copy .env.example jadi .env, lalu isi "
        f"{env_name}=xxx\n"
        "  - restart kernel supaya .env di-reload\n"
        "Kalau di GOOGLE COLAB:\n"
        "  - klik ikon kunci (🔑) di sidebar kiri → Add new secret\n"
        f"  - Name: {env_name}, Value: key kamu, lalu aktifkan 'Notebook access'\n"
        f"Daftar key gratis di {signup_url}"
    )


def groq_client() -> OpenAI:
    """Return OpenAI-compatible client untuk Groq.

    Key dibaca dari Colab Secrets (kalau di Colab) atau .env (kalau lokal).
    Daftar gratis di https://console.groq.com.
    """
    api_key = get_secret("GROQ_API_KEY")
    if not api_key:
        raise _missing_key_error("GROQ_API_KEY", "https://console.groq.com/keys")
    return OpenAI(api_key=api_key, base_url=GROQ_BASE_URL)


def openrouter_client() -> OpenAI:
    """Return OpenAI-compatible client untuk OpenRouter (fallback).

    Key dibaca dari Colab Secrets (kalau di Colab) atau .env (kalau lokal).
    """
    api_key = get_secret("OPENROUTER_API_KEY")
    if not api_key:
        raise _missing_key_error("OPENROUTER_API_KEY", "https://openrouter.ai/keys")
    return OpenAI(api_key=api_key, base_url=OPENROUTER_BASE_URL)


# Default model id yang dipakai di repo ini
GROQ_DEFAULT_MODEL = "llama-3.1-8b-instant"
GROQ_BIG_MODEL = "llama-3.3-70b-versatile"
