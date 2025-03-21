import numpy as np
import itertools
import random

def task_func(T1, max_value=100):
    # Flatten the tuple of tuples and convert string representations to integers
    int_list = list(map(int, itertools.chain.from_iterable(T1)))
    
    # Calculate the sum of these integers
    total_sum = sum(int_list)
    
    # Generate a list of random integers with size equal to the total sum
    random_list = [random.randint(0, max_value - 1) for _ in range(total_sum)]
    
    # Calculate the 25th, 50th, and 75th percentiles
    p25 = np.percentile(random_list, 25)
    p50 = np.percentile(random_list, 50)
    p75 = np.percentile(random_list, 75)
    
    return (p25, p50, p75)
