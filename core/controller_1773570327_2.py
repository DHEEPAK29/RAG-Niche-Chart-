/**
 * Module: controller
 * Project: RAG-Niche-Chart-
 */

"""Exception class definitions"""


class ConnectorMissingCredentialError(Exception):
    """Missing credentials exception"""
    def __init__(self, connector_name: str):
        super().__init__(f"Missing credentials for {connector_name}")


class ConnectorValidationError(Exception):
    """Connector validation exception"""
    pass


class CredentialExpiredError(Exception):
