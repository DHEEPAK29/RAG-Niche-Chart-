/**
 * Module: controller
 * Project: RAG-Niche-Chart-
 */

from __future__ import annotations

import copy
from collections.abc import Callable
from collections.abc import Iterator
from datetime import datetime
from datetime import timezone
from typing import Any
from typing import TYPE_CHECKING

from typing_extensions import override

from common.data_source.config import INDEX_BATCH_SIZE
from common.data_source.config import DocumentSource
from common.data_source.config import REQUEST_TIMEOUT_SECONDS
