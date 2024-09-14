import pandas as pd
from datetime import datetime, timedelta
import os

# Define the directory and file path for the local calendar
directory = "data"
file_path = os.path.join(directory, "local_calendar.csv")

# Ensure the 'data' directory exists and create it if necessary
if not os.path.exists(directory):
    os.makedirs(directory)

# Check if the calendar CSV exists, if not, create it with headers
if not os.path.exists(file_path):
    df = pd.DataFrame(columns=["Task", "Start", "End"])
    df.to_csv(file_path, index=False)

# Load the calendar events from the CSV file
def load_calendar():
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Task", "Start", "End"])

# Add a new event to the calendar
def add_event_to_calendar(task_name, start_datetime, duration_hours):
    end_datetime = start_datetime + timedelta(hours=duration_hours)
    new_event = {
        "Task": task_name,
        "Start": start_datetime.strftime('%Y-%m-%d %H:%M:%S'),
        "End": end_datetime.strftime('%Y-%m-%d %H:%M:%S')
    }
    
    calendar = load_calendar()
    calendar = pd.concat([calendar, pd.DataFrame([new_event])], ignore_index=True)
    calendar.to_csv(file_path, index=False)
    return new_event

# View all events in the calendar
def view_calendar():
    calendar = load_calendar()
    return calendar

# Delete an event from the calendar by task name
def delete_event(task_name):
    calendar = load_calendar()
    updated_calendar = calendar[calendar["Task"] != task_name]
    updated_calendar.to_csv(file_path, index=False)
    return updated_calendar
