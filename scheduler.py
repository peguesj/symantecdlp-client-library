
"""
Scheduler
=========

Schedules tasks to retrieve incidents at set intervals.

API Documentation: https://apidocs.securitycloud.symantec.com/#/doc?id=incidentdetails
"""

import schedule
import time
from .incidents import IncidentManager
from .utils import log_info, log_error
from .config import SCHEDULE_INTERVAL

def retrieve_incidents() -> None:
    """
    Retrieve incidents since the last successful retrieval.
    """
    log_info("Starting scheduled incident retrieval.")
    incident_manager = IncidentManager()
    incidents = incident_manager.fetch_incidents_since_last_retrieval()
    if incidents:
        log_info(f"Successfully retrieved {len(incidents)} incidents.")
    else:
        log_info("No new incidents retrieved.")

def start_scheduler() -> None:
    """
    Start the scheduler to run at the specified intervals.
    """
    schedule.every(SCHEDULE_INTERVAL).minutes.do(retrieve_incidents)
    log_info(f"Scheduler started, running every {SCHEDULE_INTERVAL} minutes.")
    while True:
        schedule.run_pending()
        time.sleep(1)
