/**
 * Module: handler
 * Project: RAG-Niche-Chart-
 */

import logging
from io import BytesIO

from PIL import Image

from rag.nlp import concat_img


class LazyDocxImage:
    def __init__(self, blobs, source=None):
        self._blobs = [b for b in (blobs or []) if b]
        self.source = source
        self._pil = None

    def __bool__(self):
