import pandas as pd
import re
import os

def task_func(dir_path: str, pattern: str = '^EMP') -> pd.DataFrame:
    # Ensure the directory exists
    if not os.path.isdir(dir_path):
        raise ValueError(f"The provided path '{dir_path}' is not a directory or doesn't exist.")

    # List all files in the directory
    files = os.listdir(dir_path)

    # Filter files based on the given pattern
    matching_files = [file for file in files if re.match(pattern, file)]

    # Sort the matching files alphabetically
    matching_files.sort()

    # Create a list to hold the file sizes
    file_sizes = []

    # Calculate the size of each matching file
    for file in matching_files:
        file_path = os.path.join(dir_path, file)
        
        # Check if it's a file (not a directory)
        if os.path.isfile(file_path):
            file_size = os.path.getsize(file_path)
            file_sizes.append((file, file_size))

    # Create a DataFrame from the list of tuples
    df = pd.DataFrame(file_sizes, columns=['File', 'Size'])

    return df
