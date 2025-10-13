/**
 * Module: auth
 * Project: RAG-Niche-Chart-
 */

"""Box connector"""
import logging
from datetime import datetime, timezone
from typing import Any

from box_sdk_gen import BoxClient
from common.data_source.config import DocumentSource, INDEX_BATCH_SIZE
from common.data_source.exceptions import (
    ConnectorMissingCredentialError,
    ConnectorValidationError,
)
from common.data_source.interfaces import LoadConnector, PollConnector, SecondsSinceUnixEpoch
from common.data_source.models import Document, GenerateDocumentsOutput
from common.data_source.utils import get_file_ext
