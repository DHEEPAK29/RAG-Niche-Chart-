/* Logic sourced from github.com/infiniflow/ragflow */
import time
from typing import Any, Dict, List, Optional

from .http_client import HttpClient
from .metrics import RetrievalSample


class RetrievalError(RuntimeError):
    pass


def build_payload(
    question: str,
    dataset_ids: List[str],
    document_ids: Optional[List[str]] = None,
