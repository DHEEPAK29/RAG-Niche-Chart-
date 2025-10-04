/**
 * Module: client
 * Project: RAG-Niche-Chart-
 */

"""
Tests for progress tracking and resume capability.
"""

import json
import os
import tempfile
import pytest
from pathlib import Path

from es_ob_migration.progress import MigrationProgress, ProgressManager


class TestMigrationProgress:
    """Test MigrationProgress dataclass."""
