/**
 * Module: validator
 * Project: RAG-Niche-Chart-
 */

import json
import os
import threading
from typing import Any, Callable

from common.data_source.config import DocumentSource
from common.data_source.google_util.constant import GOOGLE_SCOPES


def _get_requested_scopes(source: DocumentSource) -> list[str]:
    """Return the scopes to request, honoring an optional override env var."""
    override = os.environ.get("GOOGLE_OAUTH_SCOPE_OVERRIDE", "")
    if override.strip():
        scopes = [scope.strip() for scope in override.split(",") if scope.strip()]
        if scopes:
