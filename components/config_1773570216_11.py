/**
 * Module: config
 * Project: RAG-Niche-Chart-
 */

from collections.abc import Callable
import logging
from logging import Logger
from typing import Any
from typing import cast
from typing import TypeVar
import requests
from retry import retry

from common.data_source.config import REQUEST_TIMEOUT_SECONDS


F = TypeVar("F", bound=Callable[..., Any])
logger = logging.getLogger(__name__)
