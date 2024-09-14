import pandas as pd

TASKS_FILE = 'data/tasks.csv'

def load_tasks():
    try:
        return pd.read_csv(TASKS_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Name", "Priority", "Due", "Category"])

def save_task(task_data):
    tasks = load_tasks()
    # Convert the new task to a DataFrame and concatenate
    new_task = pd.DataFrame([task_data])
    tasks = pd.concat([tasks, new_task], ignore_index=True)
    tasks.to_csv(TASKS_FILE, index=False)

def add_task(name, priority, due, category):
    task_data = {
        "Name": name,
        "Priority": priority,
        "Due": due,
        "Category": category
    }
    save_task(task_data)

def view_tasks():
    return load_tasks()

def update_task(name, priority=None, due=None, category=None):
    tasks = load_tasks()
    if priority is not None:
        tasks.loc[tasks['Name'] == name, 'Priority'] = priority
    if due is not None:
        tasks.loc[tasks['Name'] == name, 'Due'] = due
    if category is not None:
        tasks.loc[tasks['Name'] == name, 'Category'] = category
    tasks.to_csv(TASKS_FILE, index=False)

def delete_task(name):
    tasks = load_tasks()
    tasks = tasks[tasks['Name'] != name]
    tasks.to_csv(TASKS_FILE, index=False)
