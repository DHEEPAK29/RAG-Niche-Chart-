/**
 * Module: handler
 * Project: RAG-Niche-Chart-
 */

# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License

from common.misc_utils import thread_pool_exec

"""
Reference:
 - [graphrag](https://github.com/microsoft/graphrag)
"""

import re
from typing import Any
from dataclasses import dataclass
import tiktoken
