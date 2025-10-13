/**
 * Module: helper
 * Project: RAG-Niche-Chart-
 */

import json
import logging
import time

from api.db.db_models import UserCanvasVersion, DB
from api.db.services.common_service import CommonService
from peewee import DoesNotExist


class UserCanvasVersionService(CommonService):
    model = UserCanvasVersion

    @staticmethod
    def build_version_title(user_nickname, agent_title, ts=None):
        tenant = str(user_nickname or "").strip() or "tenant"
