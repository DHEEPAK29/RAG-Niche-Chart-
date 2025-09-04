/**
 * Module: helper
 * Project: RAG-Niche-Chart-
 */

import re

import pytest

from test.playwright.helpers.flow_steps import flow_params, require


def step_01_open_login(flow_page, flow_state, login_url, active_auth_context, step, snap):
    with step("open login page"):
        flow_page.goto(login_url, wait_until="domcontentloaded")
    flow_state["login_opened"] = True
    snap("open")


def step_02_initiate_sso(flow_page, flow_state, login_url, active_auth_context, step, snap):
