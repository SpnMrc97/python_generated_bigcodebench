import numpy as np
from functools import reduce

def task_func(list_of_pairs):
    # Extract the second element from each tuple and store in a list
    second_values = [value for _, value in list_of_pairs]
    
    # Calculate the product of the second values using functools.reduce
    product = reduce(lambda x, y: x * y, second_values)
    
    # Return the product as a single-element numpy array
    return np.array([product])
