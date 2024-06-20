
"""
State Management
================

Handles the state related to the last successful retrieval of incidents.
"""

import json
import os
from typing import Any, Dict
from .config import STATE_FILE

def load_state() -> Dict[str, Any]:
    """
    Load the state from the state file.

    Returns:
        dict: State data.
    """
    if os.path.exists(STATE_FILE):
        with open(STATE_FILE, 'r') as file:
            return json.load(file)
    return {}

def save_state(state: Dict[str, Any]) -> None:
    """
    Save the state to the state file.

    Parameters:
        state (dict): State data to be saved.
    """
    with open(STATE_FILE, 'w') as file:
        json.dump(state, file)
