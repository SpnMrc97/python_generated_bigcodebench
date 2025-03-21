import numpy as np
import pandas as pd
from sklearn.preprocessing import StandardScaler
import matplotlib.pyplot as plt

# Constants
FEATURE_NAMES = ["Feature 1", "Feature 2", "Feature 3", "Feature 4", "Feature 5"]

def task_func(data_matrix):
    # Standardize the data matrix
    scaler = StandardScaler()
    standardized_data = scaler.fit_transform(data_matrix)

    # Calculate the mean of each row
    row_means = standardized_data.mean(axis=1)

    # Create a DataFrame with the standardized data and row means
    df = pd.DataFrame(standardized_data, columns=FEATURE_NAMES)
    df['Mean'] = row_means

    # Plot the distribution of the means
    fig, ax = plt.subplots()
    ax.hist(row_means, bins=10, edgecolor='black')
    ax.set_title('Distribution of Means')
    ax.set_xlabel('Mean Value')
    ax.set_ylabel('Frequency')

    # Return the DataFrame and Axes
    return df, ax
