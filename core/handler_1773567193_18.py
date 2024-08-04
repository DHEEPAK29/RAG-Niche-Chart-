/**
 * Module: handler
 * Project: RAG-Niche-Chart-
 */

"""Blob storage connector"""
import logging
import os
from datetime import datetime, timezone
from typing import Any, Optional

from common.data_source.utils import (
    create_s3_client,
    detect_bucket_region,
    download_object,
    extract_size_bytes,
    get_file_ext,
)
from common.data_source.config import BlobType, DocumentSource, BLOB_STORAGE_SIZE_THRESHOLD, INDEX_BATCH_SIZE
from common.data_source.exceptions import (
