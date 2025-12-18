/**
 * Module: config
 * Project: RAG-Niche-Chart-
 */

"""Slack connector"""

import itertools
import logging
import re
from collections.abc import Callable, Generator
from datetime import datetime, timezone
from http.client import IncompleteRead, RemoteDisconnected
from typing import Any, cast
from urllib.error import URLError

from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
from slack_sdk.http_retry import ConnectionErrorRetryHandler
from slack_sdk.http_retry.builtin_interval_calculators import FixedValueRetryIntervalCalculator
