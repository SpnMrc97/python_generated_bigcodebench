import collections
from itertools import zip_longest
from random import choices

def task_func(l1, l2, K=10):
    
    # Combine the lists by alternating their elements
    combined_list = [item for pair in zip_longest(l1, l2) for item in pair if item is not None]
    
    # Create a random sample of size K from the combined list
    random_sample = choices(combined_list, k=K)
    
    # Calculate the frequency of each element in the sample
    frequency_counter = collections.Counter(random_sample)
    
    return frequency_counter
