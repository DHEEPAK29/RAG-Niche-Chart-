/**
 * Module: helper
 * Project: RAG-Niche-Chart-
 */

import json
import time
from typing import Any, Dict, List, Optional

from .http_client import HttpClient
from .metrics import ChatSample


class ChatError(RuntimeError):
    pass


def delete_chat(client: HttpClient, chat_id: str) -> None:
    payload = {"ids": [chat_id]}
    res = client.request_json("DELETE", "/chats", json_body=payload)
