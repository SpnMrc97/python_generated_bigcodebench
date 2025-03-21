import random
import numpy as np

def task_func(LETTERS):
    random_dict = {}
    mean_dict = {}

    for letter in LETTERS:
        # Generate a list of random integers
        random_integers = [random.randint(0, 100) for _ in range(random.randint(1, 10))]
        random_dict[letter] = random_integers
        
        # Calculate the mean using numpy
        mean_dict[letter] = np.mean(random_integers)
    
    return mean_dict
