import pandas as pd
import os

# Directory and file path
directory = "data"
file_path = os.path.join(directory, "tasks.csv")

# Load tasks from CSV
def load_tasks():
    try:
        return pd.read_csv(file_path)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Name", "Priority", "Due", "Category"])

# Save a new task to CSV
def save_task(task_data):
    tasks = load_tasks()
    new_task = pd.DataFrame([task_data])  # Create a new DataFrame for the task
    tasks = pd.concat([tasks, new_task], ignore_index=True)  # Use pd.concat instead of append
    tasks.to_csv(file_path, index=False)

# Delete a task from the CSV file
def delete_task(task_name):
    tasks = load_tasks()
    tasks = tasks[tasks["Name"] != task_name]
    tasks.to_csv(file_path, index=False)
