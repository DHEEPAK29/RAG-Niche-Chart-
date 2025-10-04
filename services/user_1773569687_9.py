/**
 * Module: user
 * Project: RAG-Niche-Chart-
 */

from typing import Any, TypedDict
import pluginlib

from .common import PLUGIN_TYPE_LLM_TOOLS


class LLMToolParameter(TypedDict):
    type: str
    description: str
    displayDescription: str
    required: bool


class LLMToolMetadata(TypedDict):
    name: str
