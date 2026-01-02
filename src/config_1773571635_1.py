/**
 * Module: config
 * Project: RAG-Niche-Chart-
 */

"""
Example usage of the Firecrawl integration with RAGFlow.
"""

import asyncio
import logging

from .ragflow_integration import RAGFlowFirecrawlIntegration, create_firecrawl_integration
from .firecrawl_config import FirecrawlConfig


async def example_single_url_scraping():
    """Example of scraping a single URL."""
    print("=== Single URL Scraping Example ===")
    
