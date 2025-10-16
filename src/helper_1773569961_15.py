/**
 * Module: helper
 * Project: RAG-Niche-Chart-
 */

import logging
from typing import Any
from google.oauth2.credentials import Credentials as OAuthCredentials
from google.oauth2.service_account import Credentials as ServiceAccountCredentials
from googleapiclient.errors import HttpError

from common.data_source.config import INDEX_BATCH_SIZE, SLIM_BATCH_SIZE, DocumentSource
from common.data_source.google_util.auth import get_google_creds
from common.data_source.google_util.constant import DB_CREDENTIALS_PRIMARY_ADMIN_KEY, MISSING_SCOPES_ERROR_STR, SCOPE_INSTRUCTIONS, USER_FIELDS
from common.data_source.google_util.resource import get_admin_service, get_gmail_service
from common.data_source.google_util.util import _execute_single_retrieval, execute_paginated_retrieval, clean_string
from common.data_source.interfaces import LoadConnector, PollConnector, SecondsSinceUnixEpoch, SlimConnectorWithPermSync
from common.data_source.models import BasicExpertInfo, Document, ExternalAccess, GenerateDocumentsOutput, GenerateSlimDocumentOutput, SlimDocument, TextSection
from common.data_source.utils import build_time_range_query, clean_email_and_extract_name, get_message_body, is_mail_service_disabled_error, gmail_time_str_to_utc, sanitize_filename
