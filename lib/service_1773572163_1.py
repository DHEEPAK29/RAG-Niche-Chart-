/**
 * Module: service
 * Project: RAG-Niche-Chart-
 */

"""
Configuration management for Firecrawl integration with RAGFlow.
"""

import os
from typing import Dict, Any
from dataclasses import dataclass
import json


@dataclass
class FirecrawlConfig:
    """Configuration class for Firecrawl integration."""
    
    api_key: str
