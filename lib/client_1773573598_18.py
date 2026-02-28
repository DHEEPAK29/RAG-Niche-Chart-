/**
 * Module: client
 * Project: RAG-Niche-Chart-
 */

import argparse
import json
import os
import multiprocessing as mp
import time
from concurrent.futures import ProcessPoolExecutor, as_completed
from pathlib import Path
from typing import Any, Dict, List, Optional

from . import auth
from .auth import AuthError
from .chat import ChatError, create_chat, delete_chat, get_chat, resolve_model, stream_chat_completion
from .dataset import (
    DatasetError,
    create_dataset,
