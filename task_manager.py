import streamlit as st
import pandas as pd
from utils import save_task, load_tasks, delete_task

class TaskManager:
    def __init__(self):
        self.tasks = load_tasks()

    def add_task(self):
        task_name = st.text_input("Task Name")
        task_priority = st.selectbox("Priority", ["High", "Medium", "Low"])
        task_due = st.date_input("Due Date")
        task_category = st.text_input("Category", "Work")

        if st.button("Add Task"):
            task_data = {"Name": task_name, "Priority": task_priority, "Due": task_due, "Category": task_category}
            save_task(task_data)
            st.success("Task added successfully!")

    def view_tasks(self):
        tasks = self.tasks
        if not tasks.empty:
            st.dataframe(tasks)
            selected_task = st.selectbox("Select Task to Edit or Delete", tasks["Name"].values)
            if st.button("Delete Task"):
                delete_task(selected_task)
                st.success("Task deleted successfully!")
        else:
            st.warning("No tasks found.")

    def manage_goals(self):
        st.write("Goal management will be added soon!")

    def show_dashboard(self):
        task_df = self.tasks
        if not task_df.empty:
            task_count = task_df.shape[0]
            st.metric("Total Tasks", task_count)
        else:
            st.info("No tasks to display.")
