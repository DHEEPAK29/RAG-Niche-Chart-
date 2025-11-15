/**
 * Module: helper
 * Project: RAG-Niche-Chart-
 */

"""
Main integration file for Firecrawl with RAGFlow.
This file provides the interface between RAGFlow and the Firecrawl plugin.
"""

import logging
from typing import List, Dict, Any

from firecrawl_connector import FirecrawlConnector
from firecrawl_config import FirecrawlConfig
from firecrawl_processor import FirecrawlProcessor, RAGFlowDocument
from firecrawl_ui import FirecrawlUIBuilder


class RAGFlowFirecrawlIntegration:
