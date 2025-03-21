import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(data='/path/to/data.csv', emp_prefix='EMP'):
    # Load the CSV data into a DataFrame
    df = pd.read_csv(data)
    
    # Ensure the necessary columns are present
    if 'Employee ID' not in df.columns or 'Age' not in df.columns:
        raise ValueError("The DataFrame must contain 'Employee ID' and 'Age' columns.")
    
    # Filter the DataFrame for employee IDs with the specified prefix
    filtered_df = df[df['Employee ID'].str.startswith(emp_prefix)]
    
    # Plot the histogram of the 'Age' column
    plt.figure(figsize=(10, 6))
    ax = sns.histplot(filtered_df['Age'], bins=10, kde=False)
    ax.set_title('Age Distribution of Filtered Employees')
    ax.set_xlabel('Age')
    ax.set_ylabel('Frequency')
    
    # Show the plot
    plt.show()
    
    return filtered_df, ax
