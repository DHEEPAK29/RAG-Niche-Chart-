/**
 * Module: service
 * Project: RAG-Niche-Chart-
 */

import json
import os
from urllib.parse import urlparse

import pytest
from playwright.sync_api import TimeoutError as PlaywrightTimeoutError
from playwright.sync_api import expect

from test.playwright.helpers.auth_selectors import (
    AUTH_STATUS,
    EMAIL_INPUT,
    NICKNAME_INPUT,
    PASSWORD_INPUT,
    REGISTER_TAB,
    SUBMIT_BUTTON,
