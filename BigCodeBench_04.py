from collections import Counter
import itertools

def task_func(d):
    # Use itertools.chain to flatten the lists
    all_numbers = itertools.chain.from_iterable(d.values())

    # Use Counter to count occurrences of each number
    count_dict = Counter(all_numbers)

    return dict(count_dict)
