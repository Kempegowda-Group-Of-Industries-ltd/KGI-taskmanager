from google.oauth2 import service_account
from googleapiclient.discovery import build
from datetime import datetime, timedelta

# Define the scopes and service account file path
SCOPES = ['https://www.googleapis.com/auth/calendar']
SERVICE_ACCOUNT_FILE = 'config/credentials.json'  # Update this path as needed

# Authenticate and create the Google Calendar service
credentials = service_account.Credentials.from_service_account_file(
    SERVICE_ACCOUNT_FILE, scopes=SCOPES)
service = build('calendar', 'v3', credentials=credentials)

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
