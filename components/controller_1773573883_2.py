/**
 * Module: controller
 * Project: RAG-Niche-Chart-
 */

"""Microsoft Teams connector"""

from typing import Any

import msal
from office365.graph_client import GraphClient
from office365.runtime.client_request_exception import ClientRequestException

from common.data_source.exceptions import (
    ConnectorValidationError,
    InsufficientPermissionsError,
    UnexpectedValidationError, ConnectorMissingCredentialError
)
from common.data_source.interfaces import (
    SecondsSinceUnixEpoch,
