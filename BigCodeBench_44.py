import pandas as pd
import numpy as np
from sklearn.preprocessing import MinMaxScaler
import matplotlib.pyplot as plt

def task_func(df):
    # Replace missing values with the column's mean
    df = df.apply(lambda x: x.fillna(x.mean()), axis=0)

    # Initialize MinMaxScaler
    scaler = MinMaxScaler()

    # Normalize the DataFrame
    df_normalized = pd.DataFrame(scaler.fit_transform(df), columns=df.columns)

    # Plot box plot for each column
    ax = df_normalized.boxplot(figsize=(10, 6), grid=False)

    plt.title('Box Plot of Normalized Columns')
    plt.ylabel('Normalized Values')

    # Show the plot
    plt.show()

    return df_normalized, ax
