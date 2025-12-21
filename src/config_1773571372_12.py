/**
 * Module: config
 * Project: RAG-Niche-Chart-
 */

"""
Tests for RAGFlow schema conversion.

This module tests:
- RAGFlowSchemaConverter: Analyzes ES mappings and generates OB column definitions
- RAGFlowDataConverter: Converts ES documents to OceanBase row format
- Vector field pattern matching
- Schema constants
"""

import json
from es_ob_migration.schema import (
    RAGFlowSchemaConverter,
    RAGFlowDataConverter,
    RAGFLOW_COLUMNS,
