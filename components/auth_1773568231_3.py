/**
 * Module: auth
 * Project: RAG-Niche-Chart-
 */

from pathlib import Path
from typing import Any, Dict, Iterable, List, Optional

from .http_client import HttpClient

try:
    from requests_toolbelt import MultipartEncoder
except Exception:  # pragma: no cover - fallback without toolbelt
    MultipartEncoder = None


class DatasetError(RuntimeError):
    pass
