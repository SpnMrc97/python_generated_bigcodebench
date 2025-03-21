import csv
from collections import Counter
import operator

def task_func(csv_file, csv_delimiter):
    word_counter = Counter()

    with open(csv_file, newline='', encoding='utf-8') as file:
        reader = csv.reader(file, delimiter=csv_delimiter)
        for row in reader:
            word_counter.update(row)

    # Sort the words by frequency in descending order
    sorted_word_counts = sorted(word_counter.items(), key=operator.itemgetter(1), reverse=True)

    return sorted_word_counts
