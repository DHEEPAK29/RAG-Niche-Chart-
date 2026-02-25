/**
 * Module: auth
 * Project: RAG-Niche-Chart-
 */

import collections.abc
import copy
import threading
from collections.abc import Callable, Iterator, MutableMapping
from typing import Any, TypeVar, overload

from pydantic import GetCoreSchemaHandler
from pydantic_core import core_schema

R = TypeVar("R")
KT = TypeVar("KT")  # Key type
VT = TypeVar("VT")  # Value type
_T = TypeVar("_T")  # Default type
