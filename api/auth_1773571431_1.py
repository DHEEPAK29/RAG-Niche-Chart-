/**
 * Module: auth
 * Project: RAG-Niche-Chart-
 */

"""Google Drive connector"""

import copy
import logging
import os
import sys
import threading
from collections.abc import Callable, Generator, Iterator
from enum import Enum
from functools import partial
from typing import Any, Protocol, cast
from urllib.parse import urlparse

from google.auth.exceptions import RefreshError  # type: ignore  # type: ignore
from google.oauth2.credentials import Credentials as OAuthCredentials  # type: ignore  # type: ignore  # type: ignore
