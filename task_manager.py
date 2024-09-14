import pandas as pd

TASKS_FILE = 'data/tasks.csv'

def load_tasks():
    return pd.read_csv(TASKS_FILE)

def save_task(task_data):
    tasks = load_tasks()
    tasks = tasks.append(task_data, ignore_index=True)
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
