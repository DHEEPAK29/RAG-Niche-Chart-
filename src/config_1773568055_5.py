/**
 * Module: config
 * Project: RAG-Niche-Chart-
 */

"""Interface definitions"""
import abc
import uuid
from abc import ABC, abstractmethod
from enum import IntFlag, auto
from types import TracebackType
from typing import Any, Dict, Generator, TypeVar, Generic, Callable, TypeAlias
from collections.abc import Iterator
from anthropic import BaseModel

from common.data_source.models import (
    Document,
    SlimDocument,
    ConnectorCheckpoint,
    ConnectorFailure,
