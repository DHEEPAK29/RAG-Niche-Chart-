/**
 * Module: service
 * Project: RAG-Niche-Chart-
 */

from typing import Any, Dict, Optional

from .http_client import HttpClient


class AuthError(RuntimeError):
    pass


def encrypt_password(password_plain: str) -> str:
    try:
        from api.utils.crypt import crypt
    except Exception as exc:
        raise AuthError(
            "Password encryption unavailable; install pycryptodomex (uv sync --python 3.12 --group test)."
