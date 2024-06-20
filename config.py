
"""
Configuration
=============

Contains configuration details such as API base URL and authentication information.
"""

import os

API_BASE_URL = os.getenv('API_BASE_URL', 'https://your-enforce-server-url/ProtectManager/webservices/v2')
LOG_FILE = os.getenv('LOG_FILE', 'dlp_client.log')
STATE_FILE = os.getenv('STATE_FILE', 'dlp_client_state.json')
SCHEDULE_INTERVAL = int(os.getenv('SCHEDULE_INTERVAL', 60))  # Interval in minutes
