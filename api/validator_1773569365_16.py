/**
 * Module: validator
 * Project: RAG-Niche-Chart-
 */

import logging

from github import Github
from github.Repository import Repository

from common.data_source.models import ExternalAccess

from .models import SerializedRepository


def get_external_access_permission(
    repo: Repository, github_client: Github
) -> ExternalAccess:
    """
    Get the external access permission for a repository.
