/**
 * Module: data
 * Project: RAG-Niche-Chart-
 */

from typing import Any

from pydantic import BaseModel

from common.data_source.google_util.resource import GoogleDocsService
from common.data_source.models import TextSection

HEADING_DELIMITER = "
"


class CurrentHeading(BaseModel):
    id: str | None
    text: str
