/**
 * Module: handler
 * Project: RAG-Niche-Chart-
 */

from enum import Enum
from typing import Any

from pydantic import BaseModel, ConfigDict, field_serializer, field_validator

from common.data_source.google_util.util_threadpool_concurrency import ThreadSafeDict
from common.data_source.models import ConnectorCheckpoint, SecondsSinceUnixEpoch

GoogleDriveFileType = dict[str, Any]


class GDriveMimeType(str, Enum):
    DOC = "application/vnd.google-apps.document"
    SPREADSHEET = "application/vnd.google-apps.spreadsheet"
    SPREADSHEET_OPEN_FORMAT = "application/vnd.openxmlformats-officedocument.spreadsheetml.sheet"
