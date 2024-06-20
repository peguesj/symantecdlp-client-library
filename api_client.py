
"""
DLP API Client
==============

Handles direct communication with the Symantec DLP Enforce API.

API Documentation: https://apidocs.securitycloud.symantec.com/#/doc?id=incidentdetails
"""

from .config import API_BASE_URL
from .utils import make_request, log_info, log_error
from .state_manager import load_state, save_state
from typing import List, Dict, Any, Optional

class DLPClient:
    """
    Client for interacting with Symantec DLP Enforce API.
    """

    def get_all_incidents(self) -> List[Dict[str, Any]]:
        """
        Retrieve all incidents.

        API Reference: https://apidocs.securitycloud.symantec.com/#/doc?id=incidentlists
        """
        url = f'{API_BASE_URL}/incidents'
        params = {
            'pageSize': 100,
            'pageNumber': 1
        }
        incidents = []
        while True:
            response = make_request('GET', url, params=params)
            incidents.extend(response.get('incidents', []))
            if not response.get('hasMore'):
                break
            params['pageNumber'] += 1
        return incidents

    def get_incident_details(self, incident_id: str) -> Dict[str, Any]:
        """
        Retrieve incident details.

        API Reference: https://apidocs.securitycloud.symantec.com/#/doc?id=incidentdetails
        """
        url = f'{API_BASE_URL}/incidents/{incident_id}'
        return make_request('GET', url)

    def get_incident_list(self, filters: Optional[Dict[str, Any]] = None) -> List[Dict[str, Any]]:
        """
        Retrieve a filtered list of incidents.

        API Reference: https://apidocs.securitycloud.symantec.com/#/doc?id=incidentlists
        """
        url = f'{API_BASE_URL}/incidentlist'
        return make_request('POST', url, json=filters)

    def get_custom_attributes(self) -> List[Dict[str, Any]]:
        """
        Retrieve custom attributes.

        API Reference: https://apidocs.securitycloud.symantec.com/#/doc?id=incidenthelper
        """
        url = f'{API_BASE_URL}/incidenthelper/customAttributes'
        return make_request('GET', url)

    def get_incidents_since_last_retrieval(self) -> List[Dict[str, Any]]:
        """
        Retrieve incidents since the last successful retrieval.

        API Reference: https://apidocs.securitycloud.symantec.com/#/doc?id=incidentlists
        """
        state = load_state()
        last_retrieval = state.get('last_successful_retrieval')
        if not last_retrieval:
            log_error("No last retrieval time found in state.")
            return []
        filters = {
            "timeRange": {
                "startTime": last_retrieval
            }
        }
        return self.get_incident_list(filters)
