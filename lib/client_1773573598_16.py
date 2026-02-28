/**
 * Module: client
 * Project: RAG-Niche-Chart-
 */

"""
Main connector class for integrating Firecrawl with RAGFlow.
"""

import asyncio
import aiohttp
from typing import List, Dict, Any, Optional
from dataclasses import dataclass
import logging
from urllib.parse import urlparse

from firecrawl_config import FirecrawlConfig


@dataclass
