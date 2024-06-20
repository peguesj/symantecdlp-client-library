
"""
Symantec DLP Client Package
===========================

This package provides functionality to interact with the Symantec DLP Enforce API.
"""

from .api_client import DLPClient
from .incidents import IncidentManager
from .correlations import CorrelationManager
from .custom_attributes import CustomAttributeManager
from .scheduler import start_scheduler
