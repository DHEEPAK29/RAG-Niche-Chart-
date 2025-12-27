/**
 * Module: controller
 * Project: RAG-Niche-Chart-
 */

import json
import re
from urllib.parse import urljoin

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

from test.playwright.helpers.debug_utils import debug
from test.playwright.helpers.response_capture import capture_response


def wait_for_path_prefix(page, prefix: str, timeout_ms: int) -> None:
    """Wait until the URL path starts with the provided prefix."""
    prefix_json = json.dumps(prefix)
    wait_js = f"""
        () => {{
