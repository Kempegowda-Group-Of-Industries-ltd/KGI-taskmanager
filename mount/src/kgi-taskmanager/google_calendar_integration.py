from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta
import os

SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'mount/src/kgi-taskmanager/config/credentials.json'  # Update path as needed

# Check if the credentials file exists
if not os.path.exists(SERVICE_ACCOUNT_FILE):
    raise FileNotFoundError(f"Service account file not found at {SERVICE_ACCOUNT_FILE}. Please check the path.")

try:
    # Authenticate and create the Google Calendar service
    credentials = service_account.Credentials.from_service_account_file(
        SERVICE_ACCOUNT_FILE, scopes=SCOPES)
    service = build('calendar', 'v3', credentials=credentials)
except Exception as e:
    raise Exception(f"Error initializing Google Calendar API: {e}")

def add_event_to_calendar(task_name, due_date):
    event = {
        'summary': task_name,
        'start': {
            'dateTime': due_date.isoformat(),
            'timeZone': 'America/Los_Angeles',
        },
        'end': {
            'dateTime': (due_date + timedelta(hours=1)).isoformat(),
            'timeZone': 'America/Los_Angeles',
        },
    }
    event = service.events().insert(calendarId='primary', body=event).execute()
    print(f'Event created: {event.get("htmlLink")}')
