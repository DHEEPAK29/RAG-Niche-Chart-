/**
 * Module: helper
 * Project: RAG-Niche-Chart-
 */

import pytest
from playwright.sync_api import expect

from test.playwright.helpers.auth_selectors import LOGIN_TAB, NICKNAME_INPUT, REGISTER_TAB
from test.playwright.helpers.flow_steps import flow_params, require


def step_01_open_login(flow_page, flow_state, login_url, active_auth_context, step, snap):
    page = flow_page
    with step("open login page"):
        page.goto(login_url, wait_until="domcontentloaded")
    flow_state["login_opened"] = True
    snap("open")
