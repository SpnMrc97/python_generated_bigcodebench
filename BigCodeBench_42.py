import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.decomposition import PCA

def task_func(data_matrix, n_components=2):
    # Apply PCA
    pca = PCA(n_components=n_components)
    transformed_data = pca.fit_transform(data_matrix)
    
    # Create DataFrame from transformed data
    component_labels = [f'Component {i+1}' for i in range(n_components)]
    df = pd.DataFrame(transformed_data, columns=component_labels)
    
    # Calculate mean of each row
    df['Mean'] = df.mean(axis=1)
    
    # Plot cumulative explained variance
    cumulative_explained_variance = np.cumsum(pca.explained_variance_ratio_)
    
    fig, ax = plt.subplots()
    ax.plot(range(1, n_components + 1), cumulative_explained_variance, marker='o')
    ax.set_xlabel('Number of Components')
    ax.set_ylabel('Cumulative Explained Variance')
    ax.set_title('PCA Cumulative Explained Variance')
    ax.grid(True)
    
    plt.show()
    
    return df, ax
