/**
 * Module: helper
 * Project: RAG-Niche-Chart-
 */



"""Confluence connector"""
import copy
import json
import logging
import time
from datetime import datetime, timezone, timedelta
from pathlib import Path
from typing import Any, cast, Iterator, Callable, Generator

import requests
from typing_extensions import override
from urllib.parse import quote
