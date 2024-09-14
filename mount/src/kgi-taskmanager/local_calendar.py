import os
import pandas as pd
from datetime import datetime, timedelta

# Directory and file path for storing events locally
CALENDAR_DIRECTORY = "/mount/src/kgi-taskmanager/data"
CALENDAR_FILE = os.path.join(CALENDAR_DIRECTORY, "local_calendar.csv")

# Ensure the calendar file exists with the correct headers
def initialize_calendar_file():
    if not os.path.exists(CALENDAR_DIRECTORY):
        os.makedirs(CALENDAR_DIRECTORY)
    
    if not os.path.exists(CALENDAR_FILE):
        # Create the CSV file with the necessary columns
        columns = ["Task", "Start", "End"]
        df = pd.DataFrame(columns=columns)
        df.to_csv(CALENDAR_FILE, index=False)
        print(f"{CALENDAR_FILE} created successfully with headers: {columns}")
    else:
        print(f"{CALENDAR_FILE} already exists.")

# Function to add an event to the local calendar
def add_event_to_calendar(task_name, due_date):
    initialize_calendar_file()  # Ensure the calendar file exists
    events = pd.read_csv(CALENDAR_FILE)
    
    # Create a new event (task) DataFrame row
    new_event = pd.DataFrame([{
        'Task': task_name,
        'Start': due_date.isoformat(),
        'End': (due_date + timedelta(hours=1)).isoformat()  # 1-hour default duration
    }])

    # Append the new event to the events DataFrame
    events = pd.concat([events, new_event], ignore_index=True)

    # Save the updated DataFrame back to the CSV
    events.to_csv(CALENDAR_FILE, index=False)
    print(f"Event '{task_name}' added to local calendar.")

# Function to view all events in the local calendar
def view_calendar():
    if os.path.exists(CALENDAR_FILE):
        return pd.read_csv(CALENDAR_FILE)
    else:
        print(f"No calendar file found at {CALENDAR_FILE}.")
        return pd.DataFrame(columns=["Task", "Start", "End"])
