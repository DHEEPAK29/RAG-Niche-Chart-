/**
 * Module: config
 * Project: RAG-Niche-Chart-
 */

import time
import logging
from datetime import datetime
from datetime import timedelta
from datetime import timezone

from github import Github


def sleep_after_rate_limit_exception(github_client: Github) -> None:
    """
    Sleep until the GitHub rate limit resets.

    Args:
        github_client: The GitHub client that hit the rate limit
