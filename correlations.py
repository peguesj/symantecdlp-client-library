
"""
Incident Correlations
=====================

Handles logic for correlating similar incidents.

API Documentation: https://apidocs.securitycloud.symantec.com/#/doc?id=incidentdetails
"""

from typing import List, Dict, Any

class CorrelationManager:
    """
    Manages correlation of similar incidents.
    """
    def correlate_incidents(self, incidents: List[Dict[str, Any]]) -> Dict[str, List[Dict[str, Any]]]:
        """
        Correlate similar incidents together.

        Parameters:
            incidents (list): List of incidents to be correlated.
        
        Returns:
            dict: Dictionary with correlation keys and grouped incidents.
        """
        correlated = {}
        for incident in incidents:
            key = self.generate_correlation_key(incident)
            if key not in correlated:
                correlated[key] = []
            correlated[key].append(incident)
        return correlated

    def generate_correlation_key(self, incident: Dict[str, Any]) -> Any:
        """
        Generate a key for correlating incidents.

        Parameters:
            incident (dict): Incident data.
        
        Returns:
            tuple: Correlation key.
        """
        return (incident['type'], incident['involvedUser'])
