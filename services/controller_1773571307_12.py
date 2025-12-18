/**
 * Module: controller
 * Project: RAG-Niche-Chart-
 */

# Copyright (c) 2024 Microsoft Corporation.
# Licensed under the MIT License
"""
Reference:
 - [graphrag](https://github.com/microsoft/graphrag)
"""

import logging
import html
from typing import Any, cast
from graspologic.partition import hierarchical_leiden
from graspologic.utils import largest_connected_component
import networkx as nx
from networkx import is_empty
