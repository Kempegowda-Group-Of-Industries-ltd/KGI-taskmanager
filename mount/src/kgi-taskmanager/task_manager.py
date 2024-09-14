import pandas as pd

# Define the file path for the tasks.csv file
TASKS_FILE = '/mount/src/kgi-taskmanager/data/tasks.csv'

# Load tasks from the CSV file
def load_tasks():
    try:
        # Load tasks from CSV, or return an empty DataFrame if not found
        return pd.read_csv(TASKS_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Name", "Priority", "Due", "Category"])

# Save a new or updated task to the CSV file
def save_task(task_data):
    tasks = load_tasks()
    # Create a DataFrame for the new task and concatenate with existing tasks
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
