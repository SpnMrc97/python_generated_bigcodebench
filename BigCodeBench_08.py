from collections import Counter
import itertools
from random import randint

def task_func(T1, RANGE=100):
    # Flatten the tuple of tuples and convert strings to integers
    integer_list = list(map(int, itertools.chain.from_iterable(T1)))
    
    # Calculate the sum of the integers
    total_sum = sum(integer_list)
    
    # Generate random integers based on the total sum
    random_numbers = [randint(0, RANGE) for _ in range(total_sum)]
    
    # Count the occurrences of each number using Counter
    counts = Counter(random_numbers)
    
    return counts
