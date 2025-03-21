import psutil
import platform

def task_func():
    # Get operating system details
    os_name = platform.system()
    
    # Get architecture details
    architecture = platform.architecture()[0]
    
    # Get memory details using psutil
    memory_info = psutil.virtual_memory()
    memory_usage_percentage = (memory_info.used / memory_info.total) * 100
    
    # Create a dictionary with the gathered information
    system_info = {
        'OS': os_name,
        'Architecture': architecture,
        'Memory Usage': f"{memory_usage_percentage:.2f}%"
    }
    
    return system_info
