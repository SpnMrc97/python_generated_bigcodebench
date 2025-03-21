import pandas as pd
import numpy as np
from sklearn.decomposition import PCA
import seaborn as sns
import matplotlib.pyplot as plt

def task_func(df: pd.DataFrame):
    # Select only the numeric columns
    numeric_df = df.select_dtypes(include=[np.number])
    
    # Fill missing values with the column mean
    filled_df = numeric_df.apply(lambda col: col.fillna(col.mean()), axis=0)
    
    # Perform PCA
    pca = PCA(n_components=2)
    principal_components = pca.fit_transform(filled_df)
    
    # Create a DataFrame for the principal components
    principal_df = pd.DataFrame(data=principal_components, columns=['Component 1', 'Component 2'])
    
    # Plot the first two principal components
    plt.figure(figsize=(8, 6))
    ax = sns.scatterplot(x='Component 1', y='Component 2', data=principal_df)
    ax.set_title('PCA of Dataset')
    ax.set_xlabel('Component 1')
    ax.set_ylabel('Component 2')
    plt.grid(True)
    plt.show()
    
    return principal_df, ax
