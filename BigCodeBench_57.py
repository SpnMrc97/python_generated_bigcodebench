import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(csv_file_path: str, title: str):
    # Load the data into a DataFrame
    df = pd.read_csv(csv_file_path)
    
    # Compute the correlation matrix
    correlation_matrix = df.corr()
    
    # Round the correlation matrix to 2 decimals
    correlation_matrix = correlation_matrix.round(2)
    
    # Set up the matplotlib figure
    plt.figure(figsize=(10, 8))
    
    # Create a heatmap using seaborn
    ax = sns.heatmap(correlation_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar_kws={'label': 'Correlation Coefficient'})
    
    # Set the title of the heatmap
    plt.title(title)
    
    # Show the plot
    plt.show()
    
    # Return the correlation matrix and the axes object
    return correlation_matrix, ax
