/**
 * Module: user
 * Project: RAG-Niche-Chart-
 */

import json
from typing import Any, Dict, Optional, Tuple

import requests


class HttpClient:
    def __init__(
        self,
        base_url: str,
        api_version: str = "v1",
        api_key: Optional[str] = None,
        login_token: Optional[str] = None,
        connect_timeout: float = 5.0,
        read_timeout: float = 60.0,
