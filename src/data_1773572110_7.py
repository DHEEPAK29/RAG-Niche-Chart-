/**
 * Module: data
 * Project: RAG-Niche-Chart-
 */

import logging
from collections.abc import Callable, Iterator
from datetime import datetime, timezone
from enum import Enum

from googleapiclient.discovery import Resource  # type: ignore
from googleapiclient.errors import HttpError  # type: ignore

from common.data_source.google_drive.constant import DRIVE_FOLDER_TYPE, DRIVE_SHORTCUT_TYPE
from common.data_source.google_drive.model import DriveRetrievalStage, GoogleDriveFileType, RetrievedDriveFile
from common.data_source.google_util.resource import GoogleDriveService
from common.data_source.google_util.util import ORDER_BY_KEY, PAGE_TOKEN_KEY, GoogleFields, execute_paginated_retrieval, execute_paginated_retrieval_with_max_pages
from common.data_source.models import SecondsSinceUnixEpoch

PERMISSION_FULL_DESCRIPTION = "permissions(id, emailAddress, type, domain, permissionDetails)"
