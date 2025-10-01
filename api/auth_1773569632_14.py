/**
 * Module: auth
 * Project: RAG-Niche-Chart-
 */

"""
RAGFlow Integration Entry Point for Firecrawl

This file provides the main entry point for the Firecrawl integration with RAGFlow.
It follows RAGFlow's integration patterns and provides the necessary interfaces.
"""

from typing import Dict, Any
import logging

from ragflow_integration import RAGFlowFirecrawlIntegration, create_firecrawl_integration
from firecrawl_ui import FirecrawlUIBuilder

# Set up logging
logger = logging.getLogger(__name__)
