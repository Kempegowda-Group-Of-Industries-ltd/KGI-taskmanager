import streamlit as st
from local_calendar import add_event_to_calendar, view_calendar
from task_manager import add_task, view_tasks, delete_task, update_task

def main():
    st.title("Task and Goal Management App")

    # Sidebar for selecting task/goal operations
    menu = ["Add Task", "View Tasks", "Delete Task", "Update Task", "View Calendar"]
    choice = st.sidebar.selectbox("Select an Operation", menu)

    # Add Task
    if choice == "Add Task":
        st.subheader("Add New Task")
        task_name = st.text_input("Task Name")
        task_priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        task_due = st.date_input("Due Date")
        task_category = st.text_input("Category")
        
        if st.button("Add Task"):
            add_task(task_name, task_priority, task_due, task_category)
            add_event_to_calendar(task_name, task_due)  # Add to local calendar
            st.success("Task added successfully!")

    # View Tasks
    elif choice == "View Tasks":
        st.subheader("View All Tasks")
        tasks = view_tasks()
        st.write(tasks)

    # Delete Task
    elif choice == "Delete Task":
        st.subheader("Delete a Task")
        task_name = st.text_input("Task Name to Delete")
        
        if st.button("Delete Task"):
            delete_task(task_name)
            st.success("Task deleted successfully!")

    # Update Task
    elif choice == "Update Task":
        st.subheader("Update a Task")
        task_name = st.text_input("Task Name to Update")
        task_priority = st.selectbox("New Priority", ["Low", "Medium", "High"], index=0)
        task_due = st.date_input("New Due Date")
        task_category = st.text_input("New Category")
        
        if st.button("Update Task"):
            update_task(task_name, task_priority, task_due, task_category)
            st.success("Task updated successfully!")

    # View Calendar
    elif choice == "View Calendar":
        st.subheader("View Calendar Events")
        events = view_calendar()
        st.write(events)

if __name__ == "__main__":
    main()
