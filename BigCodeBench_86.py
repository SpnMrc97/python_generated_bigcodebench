import numpy as np
import pandas as pd
import matplotlib.pyplot as plt

def task_func(students=["Alice", "Bob", "Charlie", "David", "Eve"], seed=42):
    # Set the random seed for reproducibility
    np.random.seed(seed)
    
    # Generate random scores
    scores = np.random.randint(0, 100, size=len(students))
    
    # Create a DataFrame
    df = pd.DataFrame({'Student': students, 'Score': scores})
    
    # Sort the DataFrame by 'Score'
    df_sorted = df.sort_values(by='Score').reset_index(drop=True)
    
    # Plot the scores
    fig, ax = plt.subplots()
    df_sorted.plot(kind='bar', x='Student', y='Score', ax=ax, color='skyblue', legend=False)
    ax.set_title('Student Scores')
    ax.set_ylabel('Score')
    ax.set_xlabel('Student')
    ax.set_xticklabels(df_sorted['Student'], rotation=45, ha='right')
    plt.tight_layout()
    
    return df_sorted, ax
