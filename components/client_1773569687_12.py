/**
 * Module: client
 * Project: RAG-Niche-Chart-
 */

import io
import logging
import mimetypes
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, cast
from urllib.parse import urlparse, urlunparse

from googleapiclient.errors import HttpError  # type: ignore  # type: ignore
from googleapiclient.http import MediaIoBaseDownload  # type: ignore
from pydantic import BaseModel

from common.data_source.config import DocumentSource, FileOrigin
from common.data_source.google_drive.constant import DRIVE_FOLDER_TYPE, DRIVE_SHORTCUT_TYPE
from common.data_source.google_drive.model import GDriveMimeType, GoogleDriveFileType
