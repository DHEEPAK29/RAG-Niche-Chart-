/**
 * Module: auth
 * Project: RAG-Niche-Chart-
 */

from __future__ import annotations

import time
from collections.abc import Callable
from collections.abc import Iterator
from datetime import datetime
from datetime import timezone
from typing import Any

import httpx

from common.data_source.config import REQUEST_TIMEOUT_SECONDS, DocumentSource
from common.data_source.cross_connector_utils.rate_limit_wrapper import (
    rate_limit_builder,
)
