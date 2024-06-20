
"""
Custom Attribute Management
===========================

Manages operations related to custom attributes.

API Documentation: https://apidocs.securitycloud.symantec.com/#/doc?id=incidenthelper
"""

from .api_client import DLPClient
from typing import List, Dict, Any

class CustomAttributeManager:
    """
    Manages custom attribute operations.
    """
    def __init__(self):
        self.client = DLPClient()

    def fetch_custom_attributes(self) -> List[Dict[str, Any]]:
        """
        Fetch custom attributes.

        API Reference: https://apidocs.securitycloud.symantec.com/#/doc?id=incidenthelper
        """
        return self.client.get_custom_attributes()
