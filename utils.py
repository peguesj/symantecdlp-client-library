
"""
Utilities
=========

Contains utility functions for making API requests, logging, and error handling.
"""

import logging
import requests
from requests.auth import HTTPBasicAuth
from typing import Any, Dict
import os

# Centralized logging configuration
def configure_logging():
    logging.basicConfig(
        filename=os.getenv('LOG_FILE', 'dlp_client.log'),
        level=logging.INFO,
        format='%(asctime)s:%(levelname)s:%(message)s'
    )

configure_logging()

def make_request(method: str, url: str, **kwargs) -> Dict[str, Any]:
    """
    Make an API request.

    Parameters:
        method (str): HTTP method (GET, POST, etc.).
        url (str): URL for the request.
        kwargs: Additional parameters for the request.
    
    Returns:
        dict: JSON response.
    
    Raises:
        RequestException: If the request fails.
    """
    try:
        auth = HTTPBasicAuth(os.getenv('USERNAME'), os.getenv('PASSWORD'))
        headers = {
            'Accept': 'application/json',
            'Content-Type': 'application/json',
        }
        response = requests.request(method, url, headers=headers, auth=auth, **kwargs)
        response.raise_for_status()
        return response.json()
    except requests.exceptions.RequestException as e:
        logging.error(f"Request failed: {e}")
        raise

def log_info(message: str) -> None:
    """
    Log an informational message.

    Parameters:
        message (str): Message to be logged.
    """
    logging.info(message)

def log_error(message: str) -> None:
    """
    Log an error message.

    Parameters:
        message (str): Message to be logged.
    """
    logging.error(message)
