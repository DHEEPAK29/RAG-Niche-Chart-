/**
 * Module: client
 * Project: RAG-Niche-Chart-
 */

from datetime import datetime, timezone
import logging
from typing import Any, Generator

import requests

from pyairtable import Api as AirtableApi

from common.data_source.config import AIRTABLE_CONNECTOR_SIZE_THRESHOLD, INDEX_BATCH_SIZE, DocumentSource
from common.data_source.exceptions import ConnectorMissingCredentialError
from common.data_source.interfaces import LoadConnector, PollConnector
from common.data_source.models import Document, GenerateDocumentsOutput, SecondsSinceUnixEpoch
from common.data_source.utils import extract_size_bytes, get_file_ext

class AirtableClientNotSetUpError(PermissionError):
