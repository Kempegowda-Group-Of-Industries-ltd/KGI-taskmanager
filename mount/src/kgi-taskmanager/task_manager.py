import pandas as pd
import os

# Directory and file path
TASKS_DIRECTORY = "/mount/src/kgi-taskmanager/data"
TASKS_FILE = os.path.join(TASKS_DIRECTORY, "tasks.csv")

# Ensure the CSV file exists
def initialize_task_file():
    if not os.path.exists(TASKS_DIRECTORY):
        os.makedirs(TASKS_DIRECTORY)
    if not os.path.exists(TASKS_FILE):
        columns = ["Name", "Priority", "Due", "Category"]
        df = pd.DataFrame(columns=columns)
        df.to_csv(TASKS_FILE, index=False)
        print(f"{TASKS_FILE} created successfully with headers: {columns}")
    else:
        print(f"{TASKS_FILE} already exists.")

initialize_task_file()

# Load tasks from CSV
def load_tasks():
    try:
        return pd.read_csv(TASKS_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Name", "Priority", "Due", "Category"])

# Save a new task to CSV
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
    tasks = tasks[tasks["Name"] != name]
    tasks.to_csv(TASKS_FILE, index=False)
