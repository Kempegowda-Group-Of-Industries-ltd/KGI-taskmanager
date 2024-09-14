import pandas as pd

GOALS_FILE = 'data/goals.csv'

def load_goals():
    return pd.read_csv(GOALS_FILE)

def save_goal(goal_data):
    goals = load_goals()
    goals = goals.append(goal_data, ignore_index=True)
    goals.to_csv(GOALS_FILE, index=False)

def add_goal(name, priority, due, category, progress):
    goal_data = {
        "Name": name,
        "Priority": priority,
        "Due": due,
        "Category": category,
        "Progress": progress
    }
    save_goal(goal_data)

def view_goals():
    return load_goals()

def update_goal(name, progress):
    goals = load_goals()
    goals.loc[goals['Name'] == name, 'Progress'] = progress
    goals.to_csv(GOALS_FILE, index=False)

def delete_goal(name):
    goals = load_goals()
    goals = goals[goals['Name'] != name]
    goals.to_csv(GOALS_FILE, index=False)
