/**
 * Module: data
 * Project: RAG-Niche-Chart-
 */

"""Dropbox connector"""

import logging
from datetime import timezone
from typing import Any

from dropbox import Dropbox
from dropbox.exceptions import ApiError, AuthError
from dropbox.files import FileMetadata, FolderMetadata

from common.data_source.config import INDEX_BATCH_SIZE, DocumentSource
from common.data_source.exceptions import (
    ConnectorMissingCredentialError,
    ConnectorValidationError,
    InsufficientPermissionsError,
