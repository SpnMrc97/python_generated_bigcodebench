import pandas as pd
import regex as re

# Constants
STOPWORDS = ["a", "an", "the", "in", "is", "are"]

def task_func(text):
    # Convert to lowercase
    text = text.lower()
    
    # Use regex to find all words
    words = re.findall(r'\b\w+\b', text)
    
    # Remove stopwords
    words = [word for word in words if word not in STOPWORDS]
    
    # Create a pandas Series and count the occurrences of each word
    word_counts = pd.Series(words).value_counts()
    
    return word_counts
