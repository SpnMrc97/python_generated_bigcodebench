import math
import itertools
from functools import reduce

def task_func(numbers):
    log_sum = 0.0
    # Loop over all possible combination lengths
    for r in range(1, len(numbers) + 1):
        # Generate all combinations of the current length
        for combination in itertools.combinations(numbers, r):
            # Calculate the product of the current combination
            product = reduce(lambda x, y: x * y, combination)
            # Add the logarithm of the product to the total sum
            log_sum += math.log(product)
    
    return log_sum
