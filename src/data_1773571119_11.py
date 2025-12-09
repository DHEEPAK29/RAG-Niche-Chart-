/**
 * Module: data
 * Project: RAG-Niche-Chart-
 */

import json
import os
from urllib.parse import urlparse

import pytest
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import expect

from test.playwright.helpers.auth_selectors import (
    AUTH_ACTIVE_FORM,
    AUTH_STATUS,
    EMAIL_INPUT,
    PASSWORD_INPUT,
    SUBMIT_BUTTON,
)
