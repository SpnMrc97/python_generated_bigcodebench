import configparser
import os
import shutil

def task_func(config_file_path, archive_dir='/home/user/archive'):
    
    # Check if the configuration file exists
    if not os.path.isfile(config_file_path):
        raise FileNotFoundError(f"Configuration file '{config_file_path}' does not exist.")
    
    # Initialize ConfigParser and read the configuration file
    config = configparser.ConfigParser()
    config.read(config_file_path)
    
    # Retrieve the project directory from the configuration file
    try:
        project_dir = config.get('Project', 'directory')
    except (configparser.NoSectionError, configparser.NoOptionError) as e:
        raise Exception("Configuration file is missing 'Project' section or 'directory' option.") from e
    
    # Check if the project directory exists
    if not os.path.isdir(project_dir):
        raise FileNotFoundError(f"Project directory '{project_dir}' does not exist.")
    
    # Ensure the archive directory exists, create it if it doesn't
    os.makedirs(archive_dir, exist_ok=True)
    
    # Determine the basename for the ZIP file
    project_basename = os.path.basename(os.path.normpath(project_dir))
    zip_file_path = os.path.join(archive_dir, f"{project_basename}.zip")
    
    # Create a ZIP archive of the project directory
    try:
        shutil.make_archive(os.path.join(archive_dir, project_basename), 'zip', project_dir)
    except Exception as e:
        raise Exception(f"Failed to create ZIP archive '{zip_file_path}'.") from e
    
    return True
