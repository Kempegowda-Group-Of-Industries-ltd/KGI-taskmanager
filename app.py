import streamlit as st
from task_manager import add_task, view_tasks, update_task, delete_task

def main():
    st.title("KGI - Task Management")

    selection = st.sidebar.selectbox(
        "Select Option",
        ["Add Task", "View Tasks", "Edit Task", "Delete Task"]
    )

    if selection == "Add Task":
        st.title("Add New Task")
        task_name = st.text_input("Task Name")
        task_priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        task_due = st.date_input("Due Date")
        task_category = st.text_input("Category")
        if st.button("Add Task"):
            add_task(task_name, task_priority, task_due, task_category)
            st.success("Task added successfully!")

    elif selection == "View Tasks":
        st.title("Your Tasks")
        tasks = view_tasks()
        st.write(tasks)

    elif selection == "Edit Task":
        st.title("Edit Task")
        task_name = st.text_input("Task Name to Edit")
        task_priority = st.selectbox("New Priority (Optional)", ["Low", "Medium", "High"], index=0)
        task_due = st.date_input("New Due Date (Optional)", value=None)
        task_category = st.text_input("New Category (Optional)", value="")
        if st.button("Update Task"):
            update_task(task_name, 
                         priority=task_priority if task_priority else None, 
                         due=task_due if task_due else None,
                         category=task_category if task_category else None)
            st.success("Task updated successfully!")

    elif selection == "Delete Task":
        st.title("Delete Task")
        task_name = st.text_input("Task Name to Delete")
        if st.button("Delete Task"):
            delete_task(task_name)
            st.success("Task deleted successfully!")

if __name__ == "__main__":
    main()
