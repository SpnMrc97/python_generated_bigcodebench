import pandas as pd
import os
import numpy as np
import ast
import matplotlib.pyplot as plt

def task_func(directory):
    # Get list of all CSV files in the directory
    csv_files = [f for f in os.listdir(directory) if f.endswith('.csv')]
    
    # If no CSV files are found, return an empty DataFrame and None
    if not csv_files:
        return pd.DataFrame(columns=['email', 'list', 'sum', 'mean', 'median']), None
    
    # Find the CSV file with the longest filename
    longest_filename = max(csv_files, key=len)
    file_path = os.path.join(directory, longest_filename)
    
    # Load the CSV file into a DataFrame
    df = pd.read_csv(file_path)
    
    # Ensure the DataFrame has the required columns
    if 'email' not in df.columns or 'list' not in df.columns:
        raise ValueError("CSV file must contain 'email' and 'list' columns")
    
    # Convert the 'list' column from string representation to actual lists
    df['list'] = df['list'].apply(ast.literal_eval)
    
    # Calculate sum, mean, and median for each list
    df['sum'] = df['list'].apply(np.sum)
    df['mean'] = df['list'].apply(np.mean)
    df['median'] = df['list'].apply(np.median)
    
    # Plot a histogram of the medians
    if not df.empty:
        ax = df['median'].plot.hist(bins=10, alpha=0.7)
        plt.title('Histogram of Medians')
        plt.xlabel('Median Values')
        plt.ylabel('Frequency')
        plt.grid(True)
        plt.show()
    else:
        ax = None
    
    return df, ax