import time
from datetime import datetime
import random
import matplotlib.pyplot as plt

# Constants
DATE_FORMAT = "%Y-%m-%d %H:%M:%S"

def task_func(n, output_path=None):
    # Generate n random Unix timestamps
    timestamps = [random.randint(0, int(time.time())) for _ in range(n)]
    
    # Convert timestamps to formatted strings
    formatted_timestamps = [datetime.utcfromtimestamp(ts).strftime(DATE_FORMAT) for ts in timestamps]
    
    # Plot histogram
    plt.hist(timestamps, bins=30, color='blue', alpha=0.7)
    plt.xlabel('Unix Timestamp')
    plt.ylabel('Frequency')
    plt.title('Histogram of Random Unix Timestamps')
    
    # Save or display the plot based on the output_path parameter
    if output_path:
        plt.savefig(output_path)
    else:
        plt.show()
    
    return formatted_timestamps
