import numpy as np
import math
import pandas as pd

def haversine_distance(coord1, coord2):
    # Radius of the Earth in kilometers
    R = 6371.0

    # Convert latitude and longitude from degrees to radians
    lat1, lon1 = map(math.radians, coord1)
    lat2, lon2 = map(math.radians, coord2)

    # Compute differences
    dlat = lat2 - lat1
    dlon = lon2 - lon1

    # Haversine formula
    a = math.sin(dlat / 2)**2 + math.cos(lat1) * math.cos(lat2) * math.sin(dlon / 2)**2
    c = 2 * math.atan2(math.sqrt(a), math.sqrt(1 - a))

    # Distance in kilometers
    distance = R * c
    return distance

def task_func(data, target, k):
    if not isinstance(k, int) or k < 0:
        raise ValueError("'k' must be a non-negative integer.")

    # Calculate distances from the target to each point in the dataset
    distances = data.apply(lambda row: haversine_distance((row['Latitude'], row['Longitude']), target), axis=1)

    # Combine the distances with the original data
    data_with_distances = data.copy()
    data_with_distances['Distance'] = distances

    # Sort by distance and select the top 'k' nearest neighbors
    nearest_neighbors = data_with_distances.nsmallest(k, 'Distance')[['Latitude', 'Longitude']]

    return nearest_neighbors.values.tolist()
