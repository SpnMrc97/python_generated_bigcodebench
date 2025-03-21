import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
from sklearn.cluster import KMeans

def task_func(data, n_clusters=3):
    # Validate inputs
    if not isinstance(data, pd.DataFrame):
        raise ValueError("Input data must be a pandas DataFrame.")
    if not isinstance(n_clusters, int) or n_clusters <= 1:
        raise ValueError("n_clusters must be an integer greater than 1.")

    # Perform K-means clustering
    kmeans = KMeans(n_clusters=n_clusters, random_state=42)
    kmeans.fit(data)
    cluster_labels = kmeans.labels_
    centroids = kmeans.cluster_centers_

    # Plotting
    fig, ax = plt.subplots(figsize=(8, 6))
    scatter = ax.scatter(data.iloc[:, 0], data.iloc[:, 1], c=cluster_labels, cmap='viridis', alpha=0.6, edgecolor='w', s=100)
    ax.scatter(centroids[:, 0], centroids[:, 1], c='red', s=200, marker='X', label='Centroids')
    ax.set_title('K-Means Clustering')
    ax.set_xlabel(data.columns[0])
    ax.set_ylabel(data.columns[1])
    ax.legend()
    
    plt.show()

    return cluster_labels, ax
