/**
 * Module: helper
 * Project: RAG-Niche-Chart-
 */

"""
Content processor for converting Firecrawl output to RAGFlow document format.
"""

import re
import hashlib
from typing import List, Dict, Any
from dataclasses import dataclass
import logging
from datetime import datetime

from firecrawl_connector import ScrapedContent


@dataclass
