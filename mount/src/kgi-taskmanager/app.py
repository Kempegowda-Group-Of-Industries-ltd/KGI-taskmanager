import streamlit as st
from local_calendar import add_event_to_calendar, view_calendar, delete_event
import pandas as pd
from datetime import datetime

# Function to inject custom CSS into the Streamlit app
def add_custom_css():
    st.markdown("""
        <style>
            /* Styling for the KGI Task Manager */
            body {
                font-family: 'Roboto', sans-serif;
            }

            h1, h2, h3 {
                color: #004aad;
            }

            .stButton>button {
                background-color: #004aad;
                color: white;
                border: none;
                padding: 10px 20px;
                border-radius: 5px;
            }

            .stButton>button:hover {
                background-color: #003a8c;
            }

            .stTextInput input, .stDateInput input {
                border: 2px solid #004aad;
                border-radius: 5px;
                padding: 5px;
            }
        </style>
    """, unsafe_allow_html=True)

# Set up the Streamlit app layout
def main():
    # Set the page config at the start
    st.set_page_config(page_title="Local Calendar", layout="wide")
    
    # Inject custom CSS
    add_custom_css()

    st.title("📅 Local Calendar System")

    # Sidebar Menu
    menu = ["Add Event", "View Calendar", "Delete Event"]
    choice = st.sidebar.selectbox("Menu", menu)

    # 1. Add Event Section
    if choice == "Add Event":
        st.subheader("Add New Event")
        task_name = st.text_input("Event Name")
        start_date = st.date_input("Start Date", datetime.now())
        start_time = st.time_input("Start Time", datetime.now().time())
        duration_hours = st.number_input("Duration (hours)", min_value=1, max_value=12, value=1)

        # Combine date and time for the event start
        start_datetime = datetime.combine(start_date, start_time)

        if st.button("Add Event"):
            new_event = add_event_to_calendar(task_name, start_datetime, duration_hours)
            st.success(f"Event '{task_name}' added successfully!")
            st.write(new_event)

    # 2. View Calendar Section
    elif choice == "View Calendar":
        st.subheader("All Calendar Events")
        events = view_calendar()

        if not events.empty:
            st.dataframe(events)
        else:
            st.info("No events found. Please add some events.")

    # 3. Delete Event Section
    elif choice == "Delete Event":
        st.subheader("Delete an Event")
        events = view_calendar()

        if not events.empty:
            task_name = st.selectbox("Select Event to Delete", events["Task"].unique())
            if st.button("Delete Event"):
                updated_events = delete_event(task_name)
                st.success(f"Event '{task_name}' deleted successfully!")
                st.write(updated_events)
        else:
            st.info("No events available to delete.")

# Run the app
if __name__ == "__main__":
    main()
