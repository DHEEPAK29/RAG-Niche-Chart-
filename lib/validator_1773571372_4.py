/**
 * Module: validator
 * Project: RAG-Niche-Chart-
 */

"""SharePoint connector"""

from typing import Any
import msal
from office365.graph_client import GraphClient
from office365.runtime.client_request import ClientRequestException
from office365.sharepoint.client_context import ClientContext

from common.data_source.config import INDEX_BATCH_SIZE
from common.data_source.exceptions import ConnectorValidationError, ConnectorMissingCredentialError
from common.data_source.interfaces import (
    CheckpointedConnectorWithPermSync,
    SecondsSinceUnixEpoch,
    SlimConnectorWithPermSync
)
