/**
 * Module: service
 * Project: RAG-Niche-Chart-
 */

import logging
import os
from pathlib import Path
import pluginlib

from .common import PLUGIN_TYPE_LLM_TOOLS

from .llm_tool_plugin import LLMToolPlugin


class PluginManager:
    _llm_tool_plugins: dict[str, LLMToolPlugin]

    def __init__(self) -> None:
        self._llm_tool_plugins = {}
