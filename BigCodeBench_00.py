import itertools
from random import shuffle

def task_func(numbers=list(range(1, 11))):
    all_permutations = itertools.permutations(numbers)
    
    total_sum = 0
    count = 0
    
    for perm in all_permutations:
        perm_list = list(perm)
        shuffle(perm_list)  # Shuffle the permutation
        
        # Calculate the sum of absolute differences
        sum_of_diff = sum(abs(perm_list[i] - perm_list[i + 1]) for i in range(len(perm_list) - 1))
        
        total_sum += sum_of_diff
        count += 1
    
    if count == 0:
        return 0.0
    
    # Calculate the average
    average_of_sums = total_sum / count
    return average_of_sums
