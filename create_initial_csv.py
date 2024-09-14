import os
import pandas as pd


# Define the directory and file path
directory = "data"
file_path = os.path.join(directory, "tasks.csv")

# Create the 'data' directory if it doesn't exist
if not os.path.exists(directory):
    os.makedirs(directory)

# Check if the tasks.csv file exists, if not, create it
if not os.path.exists(file_path):
    # Define the columns
    columns = ["Name", "Priority", "Due", "Category"]
    
    # Create an empty DataFrame with the required columns
    df = pd.DataFrame(columns=columns)
    
    # Save the empty DataFrame to CSV
    df.to_csv(file_path, index=False)
    print(f"{file_path} created successfully with headers: {columns}")
else:
    print(f"{file_path} already exists.")
