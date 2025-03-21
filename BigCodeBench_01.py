import collections
import random
import string

def task_func(length=100):
    
    if length < 0:
        raise ValueError("Length must be a non-negative integer")

    # Create a pool of uppercase and lowercase letters
    letters = string.ascii_letters  # 'abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'

    # Generate a random string of the specified length
    random_string = ''.join(random.choice(letters) for _ in range(length))

    # Count the occurrences of each character in the string
    char_count = collections.Counter(random_string)

    return dict(char_count)
