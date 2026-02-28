/**
 * Module: controller
 * Project: RAG-Niche-Chart-
 */

import copy
import logging
import time
from collections.abc import Callable
from collections.abc import Iterator
from typing import Any

import requests
from pydantic import BaseModel
from requests.exceptions import HTTPError
from typing_extensions import override

from common.data_source.config import ZENDESK_CONNECTOR_SKIP_ARTICLE_LABELS, DocumentSource
from common.data_source.exceptions import ConnectorValidationError, CredentialExpiredError, InsufficientPermissionsError
from common.data_source.html_utils import parse_html_page_basic
