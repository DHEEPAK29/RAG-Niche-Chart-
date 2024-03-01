/* Logic sourced from github.com/infiniflow/ragflow */
"""WebDAV connector"""
import logging
import os
from datetime import datetime, timezone
from typing import Any, Optional

from webdav4.client import Client as WebDAVClient

from common.data_source.utils import (
    get_file_ext,
)
from common.data_source.config import DocumentSource, INDEX_BATCH_SIZE, BLOB_STORAGE_SIZE_THRESHOLD
from common.data_source.exceptions import (
    ConnectorMissingCredentialError,
    ConnectorValidationError,
