/**
 * Module: data
 * Project: RAG-Niche-Chart-
 */

from collections.abc import Iterator
import time
from datetime import datetime
import logging
from typing import Any, Dict
import asana
import requests
from common.data_source.config import CONTINUE_ON_CONNECTOR_FAILURE, INDEX_BATCH_SIZE, DocumentSource
from common.data_source.interfaces import LoadConnector, PollConnector
from common.data_source.models import Document, GenerateDocumentsOutput, SecondsSinceUnixEpoch
from common.data_source.utils import extract_size_bytes, get_file_ext



# https://github.com/Asana/python-asana/tree/master?tab=readme-ov-file#documentation-for-api-endpoints
