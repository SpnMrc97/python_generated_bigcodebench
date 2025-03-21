import os
import re

def task_func(pattern, log_dir='/var/log/'):
    try:
        # List all files in the specified directory
        files = os.listdir(log_dir)
        
        # Filter files that match the regex pattern
        matching_files = [f for f in files if re.match(pattern, f)]
        
        if not matching_files:
            return None
        
        # Get the full paths for the matching files
        full_paths = [os.path.join(log_dir, f) for f in matching_files]
        
        # Find the latest file based on modification time
        latest_file = max(full_paths, key=os.path.getmtime)
        
        return latest_file
    
    except FileNotFoundError:
        print(f"Directory {log_dir} not found.")
        return None
    except PermissionError:
        print(f"Permission denied for accessing {log_dir}.")
        return None
    except Exception as e:
        print(f"An error occurred: {e}")
        return None
