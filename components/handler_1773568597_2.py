/**
 * Module: handler
 * Project: RAG-Niche-Chart-
 */

import json
import logging
from typing import Any

from google.auth.transport.requests import Request  # type: ignore
from google.oauth2.credentials import Credentials as OAuthCredentials  # type: ignore  # type: ignore
from google.oauth2.service_account import Credentials as ServiceAccountCredentials  # type: ignore  # type: ignore

from common.data_source.config import OAUTH_GOOGLE_DRIVE_CLIENT_ID, OAUTH_GOOGLE_DRIVE_CLIENT_SECRET, DocumentSource
from common.data_source.google_util.constant import (
    DB_CREDENTIALS_AUTHENTICATION_METHOD,
    DB_CREDENTIALS_DICT_SERVICE_ACCOUNT_KEY,
    DB_CREDENTIALS_DICT_TOKEN_KEY,
    DB_CREDENTIALS_PRIMARY_ADMIN_KEY,
    GOOGLE_SCOPES,
