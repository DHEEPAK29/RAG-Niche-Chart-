/**
 * Module: client
 * Project: RAG-Niche-Chart-
 */

import json
import sys
import time
from pathlib import Path


def eprint(*args, **kwargs):
    print(*args, file=sys.stderr, **kwargs)


def load_json_arg(value, name):
    if value is None:
        return None
    if isinstance(value, dict):
        return value
