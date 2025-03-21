import numpy as np
import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df):
    # Replace NaN values with the column mean
    df_filled = df.copy()
    for column in df_filled.select_dtypes(include=[np.number]).columns:
        mean_value = df_filled[column].mean()
        df_filled[column].fillna(mean_value, inplace=True)

    # Get statistics description
    description = df_filled.describe()

    # Plot distribution for each numeric column
    plots = []
    numeric_columns = df_filled.select_dtypes(include=[np.number]).columns
    for column in numeric_columns:
        ax = sns.histplot(df_filled[column], bins=10, kde=True)
        ax.set_title(f'Distribution of {column}')
        plt.show()
        plots.append(ax)
        plt.clf()  # Clear the figure for the next plot

    return description, plots
