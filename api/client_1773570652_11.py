/**
 * Module: client
 * Project: RAG-Niche-Chart-
 */

# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License
"""
Reference:
 - [graphrag](https://github.com/microsoft/graphrag)
"""

from typing import Any
import numpy as np
import networkx as nx
from dataclasses import dataclass
from rag.graphrag.general.leiden import stable_largest_connected_component
import graspologic as gc
