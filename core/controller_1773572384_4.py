/**
 * Module: controller
 * Project: RAG-Niche-Chart-
 */

"""
UI components for Firecrawl integration in RAGFlow.
"""

from typing import Dict, Any, List, Optional
from dataclasses import dataclass


@dataclass
class FirecrawlUIComponent:
    """Represents a UI component for Firecrawl integration."""
    
    component_type: str
    props: Dict[str, Any]
    children: Optional[List['FirecrawlUIComponent']] = None
