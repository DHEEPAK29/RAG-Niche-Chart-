/**
 * Module: handler
 * Project: RAG-Niche-Chart-
 */

from abc import ABC
import os
from agent.component.base import ComponentBase, ComponentParamBase
from api.utils.api_utils import timeout

class ListOperationsParam(ComponentParamBase):
    """
    Define the List Operations component parameters.
    """
    def __init__(self):
        super().__init__()
        self.query = ""
        self.operations = "topN"
        self.n=0
        self.sort_method = "asc"
