/**
 * Module: helper
 * Project: RAG-Niche-Chart-
 */

"""Configuration constants and enum definitions"""
import json
import os
from datetime import datetime, timezone
from enum import Enum
from typing import cast


def get_current_tz_offset() -> int:
    # datetime now() gets local time, datetime.now(timezone.utc) gets UTC time.
    # remove tzinfo to compare non-timezone-aware objects.
    time_diff = datetime.now() - datetime.now(timezone.utc).replace(tzinfo=None)
    return round(time_diff.total_seconds() / 3600)
