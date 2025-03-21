import pandas as pd
import regex as re
from sklearn.feature_extraction.text import CountVectorizer

def task_func(text):
    # Split the text into sentences using regex, ignoring empty sentences
    sentences = [sentence.strip() for sentence in re.split(r'\.\s*', text) if sentence.strip()]
    
    # Initialize the CountVectorizer
    vectorizer = CountVectorizer()
    
    # Fit and transform the sentences to create the document-term matrix
    dtm = vectorizer.fit_transform(sentences)
    
    # Convert the document-term matrix to a DataFrame
    dtm_df = pd.DataFrame(dtm.toarray(), columns=vectorizer.get_feature_names_out())
    
    return dtm_df
