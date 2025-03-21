import random
import statistics

def task_func(LETTERS):
    # Create the initial dictionary with random integers
    random_dict = {letter: [random.randint(1, 100) for _ in range(random.randint(5, 10))] for letter in LETTERS}
    
    # Calculate the mean for each list of integers and sort the dictionary by these means in descending order
    sorted_dict = dict(sorted(random_dict.items(), key=lambda item: statistics.mean(item[1]), reverse=True))
    
    return sorted_dict
