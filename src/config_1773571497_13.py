/**
 * Module: config
 * Project: RAG-Niche-Chart-
 */

"""Discord connector"""

import asyncio
import logging
import os
from datetime import datetime, timezone
from typing import Any, AsyncIterable, Iterable

from discord import Client, MessageType
from discord.channel import TextChannel, Thread
from discord.flags import Intents
from discord.message import Message as DiscordMessage

from common.data_source.config import INDEX_BATCH_SIZE, DocumentSource
from common.data_source.exceptions import ConnectorMissingCredentialError
