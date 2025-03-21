import pandas as pd
import numpy as np
from sklearn.preprocessing import StandardScaler
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df):
    # Fill missing values with the column mean
    df_filled = df.fillna(df.mean())

    # Select numeric columns for scaling
    numeric_cols = df_filled.select_dtypes(include=[np.number]).columns

    # Standardize the numeric columns
    scaler = StandardScaler()
    df_scaled = df_filled.copy()
    df_scaled[numeric_cols] = scaler.fit_transform(df_filled[numeric_cols])

    # Compute the correlation matrix
    corr_matrix = df_scaled.corr()

    # Generate a heatmap of the correlation matrix
    plt.figure(figsize=(10, 8))
    heatmap = sns.heatmap(corr_matrix, annot=True, fmt=".2f", cmap='coolwarm', cbar=True)

    # Return the standardized DataFrame and the heatmap
    return df_scaled, heatmap
