import os
import pandas as pd

# Define the directory and file path
TASKS_DIRECTORY = "/mount/src/kgi-taskmanager/data"
TASKS_FILE = os.path.join(TASKS_DIRECTORY, "tasks.csv")

# Function to ensure the tasks.csv file is created with the required headers
def initialize_task_file():
    # Create the 'data' directory if it doesn't exist
    if not os.path.exists(TASKS_DIRECTORY):
        os.makedirs(TASKS_DIRECTORY)

    # Check if the tasks.csv file exists, if not, create it
    if not os.path.exists(TASKS_FILE):
        # Define the columns
        columns = ["Name", "Priority", "Due", "Category"]
        
        # Create an empty DataFrame with the required columns
        df = pd.DataFrame(columns=columns)
        
        # Save the empty DataFrame to CSV
        df.to_csv(TASKS_FILE, index=False)
        print(f"{TASKS_FILE} created successfully with headers: {columns}")
    else:
        print(f"{TASKS_FILE} already exists.")

# Call the initialize_task_file() when the script is loaded
initialize_task_file()

# Load tasks from the CSV file
def load_tasks():
    try:
        return pd.read_csv(TASKS_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Name", "Priority", "Due", "Category"])

# Save a new or updated task to the CSV file
def save_task(task_data):
    tasks = load_tasks()
    new_task = pd.DataFrame([task_data])
    tasks = pd.concat([tasks, new_task], ignore_index=True)
    tasks.to_csv(TASKS_FILE, index=False)

# Add a task to the task manager
def add_task(name, priority, due, category):
    task_data = {
        "Name": name,
        "Priority": priority,
        "Due": due,
        "Category": category
    }
    save_task(task_data)

# View tasks stored in the task manager
def view_tasks():
    return load_tasks()

# Update an existing task by its name
def update_task(name, priority=None, due=None, category=None):
    tasks = load_tasks()
    if priority is not None:
        tasks.loc[tasks['Name'] == name, 'Priority'] = priority
    if due is not None:
        tasks.loc[tasks['Name'] == name, 'Due'] = due
    if category is not None:
        tasks.loc[tasks['Name'] == name, 'Category'] = category
    tasks.to_csv(TASKS_FILE, index=False)

# Delete a task from the task manager
def delete_task(name):
    tasks = load_tasks()
    tasks = tasks[tasks['Name'] != name]
    tasks.to_csv(TASKS_FILE, index=False)
