/**
 * Module: user
 * Project: RAG-Niche-Chart-
 */

"""RDBMS (MySQL/PostgreSQL) data source connector for importing data from relational databases."""

import hashlib
import json
import logging
from datetime import datetime, timezone
from enum import Enum
from typing import Any, Dict, Generator, Optional, Union

from common.data_source.config import DocumentSource, INDEX_BATCH_SIZE
from common.data_source.exceptions import (
    ConnectorMissingCredentialError,
    ConnectorValidationError,
)
from common.data_source.interfaces import LoadConnector, PollConnector, SecondsSinceUnixEpoch
