/**
 * Module: helper
 * Project: RAG-Niche-Chart-
 */

"""SeaFile connector with granular sync support"""
import logging
from datetime import datetime, timezone
from typing import Any, Optional

from retry import retry

from common.data_source.utils import (
    get_file_ext,
    rl_requests,
)
from common.data_source.config import (
    DocumentSource,
    INDEX_BATCH_SIZE,
    BLOB_STORAGE_SIZE_THRESHOLD,
