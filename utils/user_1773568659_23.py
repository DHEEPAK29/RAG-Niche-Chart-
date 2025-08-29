/**
 * Module: user
 * Project: RAG-Niche-Chart-
 */

import pytest

from test.playwright.helpers.flow_context import FlowContext
from test.playwright.helpers.flow_steps import flow_params, require


def step_01_open_login(ctx: FlowContext, step, snap):
    page = ctx.page
    with step("navigate to login page"):
        response = page.goto(ctx.smoke_login_url, wait_until="domcontentloaded")
    ctx.state["smoke_opened"] = True
    ctx.state["smoke_response"] = response


def step_02_validate_page(ctx: FlowContext, step, snap):
