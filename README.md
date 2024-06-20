# Symantec DLP Client Package

This package provides functionality to interact with the Symantec DLP Enforce API. It includes modules for retrieving incidents, managing custom attributes, correlating incidents, and scheduling regular tasks to fetch incidents. The package follows best practices for error handling, logging, and configuration management.

## Table of Contents

- [Installation](#installation)
- [Configuration](#configuration)
- [Usage](#usage)
  - [Initializing the Client](#initializing-the-client)
  - [Fetching Incidents](#fetching-incidents)
  - [Fetching Incident Details](#fetching-incident-details)
  - [Fetching Custom Attributes](#fetching-custom-attributes)
  - [Correlating Incidents](#correlating-incidents)
  - [Scheduling Incident Retrieval](#scheduling-incident-retrieval)
- [Environment Variables](#environment-variables)
- [Error Handling](#error-handling)
- [Logging](#logging)
- [License](#license)

## Installation

To install the package, download the repository and run:

```bash
pip install -r requirements.txt
```

## Configuration

The package uses environment variables for configuration. Create a `.env` file in the root of your project with the following content:

```bash
API_BASE_URL=https://your-enforce-server-url/ProtectManager/webservices/v2
USERNAME=your_username
PASSWORD=your_password
LOG_FILE=dlp_client.log
STATE_FILE=dlp_client_state.json
SCHEDULE_INTERVAL=60  # Interval in minutes
```

## Usage

### Initializing the Client

```python
from symantec_dlp_client import DLPClient

client = DLPClient()
```

### Fetching Incidents

```python
# Fetch all incidents
incidents = client.get_all_incidents()
print(incidents)
```

### Fetching Incident Details

```python
# Fetch details for a specific incident
incident_id = '12345'
incident_details = client.get_incident_details(incident_id)
print(incident_details)
```

### Fetching Custom Attributes

```python
from symantec_dlp_client import CustomAttributeManager

custom_attribute_manager = CustomAttributeManager()
custom_attributes = custom_attribute_manager.fetch_custom_attributes()
print(custom_attributes)
```

### Correlating Incidents

```python
from symantec_dlp_client import CorrelationManager

correlation_manager = CorrelationManager()
correlated_incidents = correlation_manager.correlate_incidents(incidents)
for key, group in correlated_incidents.items():
    print(f"Correlation Key: {key}")
    for incident in group:
        print(incident)
```

### Scheduling Incident Retrieval

```python
from symantec_dlp_client import start_scheduler

# Start the scheduler to run at the specified intervals
start_scheduler()
```

## Environment Variables

The following environment variables are used for configuration:

- `API_BASE_URL`: The base URL of the Symantec DLP Enforce server API.
- `USERNAME`: The username for API authentication.
- `PASSWORD`: The password for API authentication.
- `LOG_FILE`: The path to the log file.
- `STATE_FILE`: The path to the state file for storing the last successful retrieval time.
- `SCHEDULE_INTERVAL`: The interval (in minutes) for scheduling incident retrieval tasks.

## Error Handling

The package includes comprehensive error handling. If an API request fails, an error message is logged and the exception is raised.

## Logging

Logging is configured centrally and logs are written to the file specified by the `LOG_FILE` environment variable. Informational messages and errors are logged with timestamps.

## License

This project is licensed under the GPL License.