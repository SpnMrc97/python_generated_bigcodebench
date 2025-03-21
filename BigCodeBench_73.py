import pandas as pd
import sqlite3
import numpy as np
import matplotlib.pyplot as plt
import ast

def task_func(db_file):
    
    # Connect to the SQLite database
    conn = sqlite3.connect(db_file)
    
    # Load data from the "EmailData" table into a DataFrame
    df = pd.read_sql_query("SELECT * FROM EmailData", conn)
    
    # Close the connection
    conn.close()
    
    # Convert the 'list' column from string representation to actual list
    df['list'] = df['list'].apply(ast.literal_eval)
    
    # Calculate sum, mean, and variance for each list
    df['sum'] = df['list'].apply(np.sum)
    df['mean'] = df['list'].apply(np.mean)
    df['var'] = df['list'].apply(np.var)
    
    # Plotting
    fig, ax = plt.subplots(figsize=(10, 6))
    index = np.arange(len(df))
    bar_width = 0.2
    
    ax.bar(index, df['sum'], bar_width, label='Sum', color='b')
    ax.bar(index + bar_width, df['mean'], bar_width, label='Mean', color='g')
    ax.bar(index + 2 * bar_width, df['var'], bar_width, label='Variance', color='r')
    
    ax.set_xlabel('Email Index')
    ax.set_ylabel('Values')
    ax.set_title('Sum, Mean, and Variance for Each Email')
    ax.set_xticks(index + bar_width)
    ax.set_xticklabels(df.index)
    ax.legend()
    
    plt.tight_layout()
    
    return df, ax
