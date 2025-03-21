import pandas as pd
import matplotlib.pyplot as plt
from scipy.stats import skew
import numpy as np

def task_func(data_matrix):
    
    # Calculate the skewness of each row
    skewness_values = [skew(row) for row in data_matrix]
    
    # Create a DataFrame with the skewness values
    df = pd.DataFrame(skewness_values, columns=['Skewness'])
    
    # Plot the distribution of skewness values
    ax = df['Skewness'].plot(kind='hist', bins=10, alpha=0.7, color='blue', edgecolor='black')
    ax.set_title('Distribution of Skewness')
    ax.set_xlabel('Skewness')
    ax.set_ylabel('Frequency')
    
    # Show the plot
    plt.show()
    
    return df, ax
