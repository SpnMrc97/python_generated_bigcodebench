import pandas as pd
import seaborn as sns
import numpy as np
from scipy.stats import zscore
import matplotlib.pyplot as plt

def task_func(data_matrix):
    # Calculate Z-scores row-wise
    z_scores = np.apply_along_axis(zscore, 1, data_matrix)
    
    # Create a DataFrame with Z-scores
    columns = [f'Feature {i+1}' for i in range(data_matrix.shape[1])]
    df = pd.DataFrame(z_scores, columns=columns)
    
    # Calculate the mean of Z-scores for each row and add as a new column
    df['Mean'] = df.mean(axis=1)
    
    # Calculate the correlation matrix
    corr_matrix = df.corr()
    
    # Plot the heatmap
    plt.figure(figsize=(10, 8))
    ax = sns.heatmap(corr_matrix, annot=True, cmap='coolwarm', cbar_kws={'label': 'Correlation Coefficient'})
    plt.title('Correlation Matrix Heatmap')
    plt.show()
    
    return df, ax
