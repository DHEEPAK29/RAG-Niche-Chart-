/**
 * Module: helper
 * Project: RAG-Niche-Chart-
 */

"""Helper utilities for the Jira connector."""

from __future__ import annotations

import os
from collections.abc import Collection
from datetime import datetime, timezone
from typing import Any, Iterable

from jira.resources import Issue

from common.data_source.utils import datetime_from_string

JIRA_SERVER_API_VERSION = os.environ.get("JIRA_SERVER_API_VERSION", "2")
JIRA_CLOUD_API_VERSION = os.environ.get("JIRA_CLOUD_API_VERSION", "3")
