/**
 * Module: auth
 * Project: RAG-Niche-Chart-
 */

import re
import time
from urllib.parse import urljoin

from playwright.sync_api import expect

from test.playwright.helpers.response_capture import capture_response

RESULT_TIMEOUT_MS = 15000


def _unique_name(prefix: str) -> str:
    return f"{prefix}-{int(time.time() * 1000)}"
