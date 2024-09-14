import streamlit as st
import pandas as pd
from task_manager import TaskManager

st.set_page_config(page_title="KGI Task Manager", layout="wide")

# Load CSS styles
with open("assets/styles.css") as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)

# Initialize task manager
task_manager = TaskManager()

# Sidebar: Navigation
st.sidebar.title("KGI Task Manager")
options = ["Dashboard", "Add Task", "View Tasks", "Manage Goals"]
selection = st.sidebar.radio("Go to", options)

# Main Content
if selection == "Dashboard":
    st.title("KGI Dashboard")
    st.write("Overview of tasks and goals.")
    task_manager.show_dashboard()

elif selection == "Add Task":
    st.title("Add New Task")
    task_manager.add_task()

elif selection == "View Tasks":
    st.title("Your Tasks")
    task_manager.view_tasks()

elif selection == "Manage Goals":
    st.title("Goal Management")
    task_manager.manage_goals()

