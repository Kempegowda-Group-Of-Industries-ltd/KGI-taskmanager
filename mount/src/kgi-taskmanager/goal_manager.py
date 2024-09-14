import pandas as pd
import os

# Directory and file path
GOALS_DIRECTORY = "/mount/src/kgi-taskmanager/data"
GOALS_FILE = os.path.join(GOALS_DIRECTORY, "goals.csv")

# Ensure the CSV file exists
def initialize_goal_file():
    if not os.path.exists(GOALS_DIRECTORY):
        os.makedirs(GOALS_DIRECTORY)
    if not os.path.exists(GOALS_FILE):
        columns = ["Name", "Priority", "Due", "Category", "Progress"]
        df = pd.DataFrame(columns=columns)
        df.to_csv(GOALS_FILE, index=False)
        print(f"{GOALS_FILE} created successfully with headers: {columns}")
    else:
        print(f"{GOALS_FILE} already exists.")

initialize_goal_file()

# Load goals from CSV
def load_goals():
    try:
        return pd.read_csv(GOALS_FILE)
    except FileNotFoundError:
        return pd.DataFrame(columns=["Name", "Priority", "Due", "Category", "Progress"])

# Save a new goal to CSV
def save_goal(goal_data):
    goals = load_goals()
    new_goal = pd.DataFrame([goal_data])
    goals = pd.concat([goals, new_goal], ignore_index=True)
    goals.to_csv(GOALS_FILE, index=False)

# Add a goal to the goal manager
def add_goal(name, priority, due, category, progress):
    goal_data = {
        "Name": name,
        "Priority": priority,
        "Due": due,
        "Category": category,
        "Progress": progress
    }
    save_goal(goal_data)

# View goals stored in the goal manager
def view_goals():
    return load_goals()

# Update an existing goal by its name
def update_goal(name, progress):
    goals = load_goals()
    goals.loc[goals['Name'] == name, 'Progress'] = progress
    goals.to_csv(GOALS_FILE, index=False)

# Delete a goal from the goal manager
def delete_goal(name):
    goals = load_goals()
    goals = goals[goals['Name'] != name]
    goals.to_csv(GOALS_FILE, index=False)
