import numpy as np
import pandas as pd
from datetime import datetime, timedelta
import matplotlib.pyplot as plt

def task_func(start_date, end_date, seed=42):
    # Set the random seed for reproducibility
    np.random.seed(seed)

    # Generate the date range
    date_range = pd.date_range(start=start_date, end=end_date)

    # Generate random sales data
    sales_data = np.random.randint(0, 501, size=len(date_range))

    # Create a DataFrame
    data = pd.DataFrame({'Date': date_range, 'Sales': sales_data})

    # Plotting
    fig, ax = plt.subplots(figsize=(12, 6))
    ax.plot(data['Date'], data['Sales'], marker='o', linestyle='-')
    ax.set_title('Sales Over Time')
    ax.set_xlabel('Date')
    ax.set_ylabel('Sales')
    ax.grid(True)

    # Show the plot
    plt.xticks(rotation=45)
    plt.tight_layout()

    return data, ax
