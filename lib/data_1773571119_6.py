/**
 * Module: data
 * Project: RAG-Niche-Chart-
 */

import logging
import re
from copy import copy
from dataclasses import dataclass
from io import BytesIO
from typing import IO

import bs4

from common.data_source.config import HTML_BASED_CONNECTOR_TRANSFORM_LINKS_STRATEGY, \
    HtmlBasedConnectorTransformLinksStrategy, WEB_CONNECTOR_IGNORED_CLASSES, WEB_CONNECTOR_IGNORED_ELEMENTS, \
    PARSE_WITH_TRAFILATURA

MINTLIFY_UNWANTED = ["sticky", "hidden"]
