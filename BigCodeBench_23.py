import numpy as np
from itertools import zip_longest

def task_func(l1, l2, THRESHOLD=0.5):
    
    # Create an interleaved list from the two input lists
    combined = [x for pair in zip_longest(l1, l2) for x in pair if x is not None]
    
    # Calculate the absolute difference from the threshold for each element
    diffs = np.abs(np.array(combined) - THRESHOLD)
    
    # Find the index of the element with the smallest difference
    min_index = np.argmin(diffs)
    
    # Return the element closest to the threshold
    return combined[min_index]
