/**
 * Module: helper
 * Project: RAG-Niche-Chart-
 */

import pytest
from playwright.sync_api import expect

from test.playwright.helpers._auth_helpers import ensure_authed
from test.playwright.helpers.flow_steps import flow_params, require
from test.playwright.helpers._next_apps_helpers import (
    RESULT_TIMEOUT_MS,
    _fill_and_save_create_modal,
    _goto_home,
    _nav_click,
    _open_create_from_list,
    _search_query_input,
    _select_first_dataset_and_save,
    _unique_name,
    _wait_for_url_or_testid,
