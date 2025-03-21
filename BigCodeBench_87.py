import pandas as pd
from random import choices, seed

def task_func(products, ratings, weights, random_seed=42):
    # Set the random seed for reproducibility
    seed(random_seed)
    
    # Generate random ratings for each product based on the provided weights
    product_ratings = choices(ratings, weights=weights, k=len(products))
    
    # Create a DataFrame from the generated data
    df = pd.DataFrame({
        'Product': products,
        'Rating': product_ratings
    })
    
    # Sort the DataFrame by 'Rating' in descending order
    df_sorted = df.sort_values(by='Rating', ascending=False).reset_index(drop=True)
    
    return df_sorted
