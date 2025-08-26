/**
 * Module: controller
 * Project: RAG-Niche-Chart-
 */

import pytest
from pathlib import Path
from tempfile import gettempdir
from time import monotonic, time

from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import expect

from test.playwright.helpers.flow_context import FlowContext
from test.playwright.helpers._auth_helpers import ensure_authed
from test.playwright.helpers.flow_steps import flow_params, require
from test.playwright.helpers._next_apps_helpers import (
    RESULT_TIMEOUT_MS,
    _fill_and_save_create_modal,
    _goto_home,
