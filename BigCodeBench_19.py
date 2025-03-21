import os
import glob
import zipfile

def task_func(directory):
    # Check if the directory exists
    if not os.path.isdir(directory):
        raise FileNotFoundError(f"The directory {directory} does not exist.")
    
    # Use glob to find all files in the directory (not including subdirectories)
    files = glob.glob(os.path.join(directory, '*'))
    # Filter out directories
    files = [f for f in files if os.path.isfile(f)]

    # Return None if there are no files to zip
    if not files:
        return None

    # Define the zip file path
    zip_path = os.path.join(directory, 'files.zip')

    # Create a zip file
    with zipfile.ZipFile(zip_path, 'w') as zipf:
        for file in files:
            # Add each file to the zip file
            zipf.write(file, os.path.basename(file))

    return zip_path
