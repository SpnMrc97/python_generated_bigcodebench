import pandas as pd
from random import randint, uniform, seed

def task_func(categories=None, months=None, random_seed=42):
    
    # Default categories and months if not provided
    default_categories = ['Electronics', 'Clothing', 'Home & Kitchen', 'Books', 'Beauty & Personal Care']
    default_months = ['January', 'February', 'March', 'April', 'May', 'June', 
                      'July', 'August', 'September', 'October', 'November', 'December']
    
    if categories is None:
        categories = default_categories
    if months is None:
        months = default_months
    
    # Validate inputs
    if not isinstance(categories, list) or not categories:
        raise ValueError("Categories must be a non-empty list.")
    if not isinstance(months, list) or not months:
        raise ValueError("Months must be a non-empty list.")
    
    # Set the random seed
    seed(random_seed)
    
    # Generate sales data
    data = []
    for month in months:
        for category in categories:
            sales = randint(100, 500) + uniform(0, 1)
            data.append({'Month': month, 'Category': category, 'Sales': sales})
    
    # Create DataFrame
    df = pd.DataFrame(data)
    return df
