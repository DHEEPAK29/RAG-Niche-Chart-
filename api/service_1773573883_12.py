/**
 * Module: service
 * Project: RAG-Niche-Chart-
 */

"""DingTalk AI Table connector for RAGFlow. By the way, "notable" is a reference to the DingTalk AI Table.

This connector ingests records from DingTalk AI Table as documents.
It first retrieves all sheets from a specified table, then fetches all records
from each sheet.

API Documentation:
- GetAllSheets: https://open.dingtalk.com/document/development/api-notable-getallsheets
- ListRecords: https://open.dingtalk.com/document/development/api-notable-listrecords
"""

import json
import logging
from datetime import datetime, timezone
from typing import Any
