
"""
Incident Management
===================

Manages operations related to incidents.

API Documentation: https://apidocs.securitycloud.symantec.com/#/doc?id=incidentdetails
"""

from .api_client import DLPClient
from .utils import log_info, log_error
from .state_manager import save_state
import datetime
from typing import List, Dict, Any, Optional

class IncidentManager:
    """
    Manages incident-related operations.
    """
    def __init__(self):
        self.client = DLPClient()

    def fetch_all_incidents(self) -> List[Dict[str, Any]]:
        """
        Fetch all incidents.
        """
        return self.client.get_all_incidents()

    def fetch_incident_details(self, incident_id: str) -> Dict[str, Any]]:
        """
        Fetch details for a specific incident.

        API Reference: https://apidocs.securitycloud.symantec.com/#/doc?id=incidentdetails
        """
        return self.client.get_incident_details(incident_id)

    def fetch_incident_list(self, filters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Fetch a filtered list of incidents.

        API Reference: https://apidocs.securitycloud.symantec.com/#/doc?id=incidentlists
        """
        return self.client.get_incident_list(filters)

    def fetch_incidents_since_last_retrieval(self) -> List[Dict[str, Any]]:
        """
        Fetch incidents since the last successful retrieval.

        API Reference: https://apidocs.securitycloud.symantec.com/#/doc?id=incidentlists
        """
        incidents = []
        try:
            incidents = self.client.get_incidents_since_last_retrieval()
            if incidents:
                log_info(f"Fetched {len(incidents)} incidents since last retrieval.")
                self.update_last_retrieval_time()
        except Exception as e:
            log_error(f"Failed to fetch incidents since last retrieval: {e}")
        return incidents

    def update_last_retrieval_time(self) -> None:
        """
        Update the last retrieval time to the current time.
        """
        state = {
            'last_successful_retrieval': datetime.datetime.utcnow().isoformat() + 'Z'
        }
        save_state(state)
