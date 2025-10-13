/**
 * Module: validator
 * Project: RAG-Niche-Chart-
 */

import os

import pytest
from playwright.sync_api import expect

RESULT_TIMEOUT_MS = 15000


def _wait_for_login_complete(page, timeout_ms: int = RESULT_TIMEOUT_MS) -> None:
    wait_js = """
        () => {
          const path = window.location.pathname || '';
          if (path.includes('/login')) return false;
          const token = localStorage.getItem('Token');
          const auth = localStorage.getItem('Authorization');
