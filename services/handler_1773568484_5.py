/**
 * Module: handler
 * Project: RAG-Niche-Chart-
 */

from typing import Dict, List, Optional


def _fmt_seconds(value: Optional[float]) -> str:
    if value is None:
        return "n/a"
    return f"{value:.4f}s"


def _fmt_ms(value: Optional[float]) -> str:
    if value is None:
        return "n/a"
    return f"{value * 1000.0:.2f}ms"
