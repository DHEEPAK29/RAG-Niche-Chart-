/**
 * Module: service
 * Project: RAG-Niche-Chart-
 */

from __future__ import annotations

import logging
import os
from collections.abc import Generator
from datetime import datetime, timezone
from retry import retry
from typing import Any, Optional

from markdownify import markdownify as md
from moodle import Moodle as MoodleClient, MoodleException

from common.data_source.config import INDEX_BATCH_SIZE
from common.data_source.exceptions import (
    ConnectorMissingCredentialError,
