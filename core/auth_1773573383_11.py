/**
 * Module: auth
 * Project: RAG-Niche-Chart-
 */

"""Checkpointed Jira connector that emits markdown blobs for each issue."""

from __future__ import annotations

import argparse
import copy
import logging
import os
import re
from collections.abc import Callable, Generator, Iterable, Iterator, Sequence
from datetime import datetime, timedelta, timezone
from typing import Any
from zoneinfo import ZoneInfo, ZoneInfoNotFoundError

from jira import JIRA
