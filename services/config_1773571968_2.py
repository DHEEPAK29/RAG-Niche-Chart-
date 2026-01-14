/**
 * Module: config
 * Project: RAG-Niche-Chart-
 */

import html
import logging
from collections.abc import Generator
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Optional
from urllib.parse import urlparse

from retry import retry

from common.data_source.config import (
    INDEX_BATCH_SIZE,
    NOTION_CONNECTOR_DISABLE_RECURSIVE_PAGE_LOOKUP,
    DocumentSource,
)
