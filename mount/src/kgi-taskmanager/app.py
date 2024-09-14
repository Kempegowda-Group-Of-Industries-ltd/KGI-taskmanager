import streamlit as st
import pandas as pd
from task_manager import add_task, view_tasks, update_task, delete_task
from goal_manager import add_goal, view_goals, update_goal, delete_goal
from google_calendar_integration import add_event_to_calendar
from datetime import datetime

def main():
    st.title("KGI Task and Goal Management")

    # Sidebar for navigation
    selection = st.sidebar.radio("Select an option", ["Add Task", "View Tasks", "Update Task", "Delete Task",
                                                     "Add Goal", "View Goals", "Update Goal", "Delete Goal"])

    if selection == "Add Task":
        st.subheader("Add New Task")
        task_name = st.text_input("Task Name")
        task_priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        task_due = st.date_input("Due Date")
        task_category = st.text_input("Category")
        if st.button("Add Task"):
            add_task(task_name, task_priority, task_due, task_category)
            add_event_to_calendar(task_name, datetime.combine(task_due, datetime.min.time()))
            st.success("Task added successfully!")

    elif selection == "View Tasks":
        st.subheader("View Tasks")
        tasks = view_tasks()
        st.write(tasks)

    elif selection == "Update Task":
        st.subheader("Update Task")
        task_name = st.text_input("Task Name to Update")
        new_priority = st.selectbox("New Priority", ["Low", "Medium", "High"])
        new_due = st.date_input("New Due Date")
        new_category = st.text_input("New Category")
        if st.button("Update Task"):
            update_task(task_name, new_priority, new_due, new_category)
            st.success("Task updated successfully!")

    elif selection == "Delete Task":
        st.subheader("Delete Task")
        task_name = st.text_input("Task Name to Delete")
        if st.button("Delete Task"):
            delete_task(task_name)
            st.success("Task deleted successfully!")

    elif selection == "Add Goal":
        st.subheader("Add New Goal")
        goal_name = st.text_input("Goal Name")
        goal_priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        goal_due = st.date_input("Due Date")
        goal_category = st.text_input("Category")
        goal_progress = st.slider("Progress", 0, 100, 0)
        if st.button("Add Goal"):
            add_goal(goal_name, goal_priority, goal_due, goal_category, goal_progress)
            st.success("Goal added successfully!")

    elif selection == "View Goals":
        st.subheader("View Goals")
        goals = view_goals()
        st.write(goals)

    elif selection == "Update Goal":
        st.subheader("Update Goal")
        goal_name = st.text_input("Goal Name to Update")
        goal_progress = st.slider("New Progress", 0, 100, 0)
        if st.button("Update Goal"):
            update_goal(goal_name, goal_progress)
            st.success("Goal updated successfully!")

    elif selection == "Delete Goal":
        st.subheader("Delete Goal")
        goal_name = st.text_input("Goal Name to Delete")
        if st.button("Delete Goal"):
            delete_goal(goal_name)
            st.success("Goal deleted successfully!")

if __name__ == "__main__":
    main()
