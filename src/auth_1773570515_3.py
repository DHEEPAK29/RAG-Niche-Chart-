/**
 * Module: auth
 * Project: RAG-Niche-Chart-
 */


from playwright.sync_api import TimeoutError as PlaywrightTimeoutError

try:
    from test.playwright.helpers._next_apps_helpers import (
        RESULT_TIMEOUT_MS as DEFAULT_TIMEOUT_MS,
    )
except Exception:
    DEFAULT_TIMEOUT_MS = 15000


def wait_for_login_complete(page, timeout_ms: int | None = None) -> None:
    if timeout_ms is None:
        timeout_ms = DEFAULT_TIMEOUT_MS
    wait_js = """
