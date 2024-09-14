import streamlit as st
from task_manager import add_task, view_tasks, update_task, delete_task
from goal_manager import add_goal, view_goals, update_goal, delete_goal

def main():
    st.title("KGI - Task and Goal Management")

    selection = st.sidebar.selectbox(
        "Select Option",
        ["Add Task", "View Tasks", "Edit Task", "Delete Task",
         "Add Goal", "View Goals", "Update Goal", "Delete Goal"]
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
            # Call update_task with parameters only if they are provided
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

    elif selection == "Add Goal":
        st.title("Add New Goal")
        goal_name = st.text_input("Goal Name")
        goal_priority = st.selectbox("Priority", ["Low", "Medium", "High"])
        goal_due = st.date_input("Due Date")
        goal_category = st.text_input("Category")
        goal_progress = st.slider("Progress", 0, 100, 0)
        if st.button("Add Goal"):
            add_goal(goal_name, goal_priority, goal_due, goal_category, goal_progress)
            st.success("Goal added successfully!")

    elif selection == "View Goals":
        st.title("Your Goals")
        goals = view_goals()
        st.write(goals)

    elif selection == "Update Goal":
        st.title("Update Goal")
        goal_name = st.text_input("Goal Name to Update")
        goal_progress = st.slider("New Progress", 0, 100, 0)
        if st.button("Update Goal"):
            update_goal(goal_name, goal_progress)
            st.success("Goal updated successfully!")

    elif selection == "Delete Goal":
        st.title("Delete Goal")
        goal_name = st.text_input("Goal Name to Delete")
        if st.button("Delete Goal"):
            delete_goal(goal_name)
            st.success("Goal deleted successfully!")

if __name__ == "__main__":
    main()
