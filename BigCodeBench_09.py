import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(list_of_pairs):
    # Create a DataFrame from the list of pairs
    df = pd.DataFrame(list_of_pairs, columns=['Category', 'Value'])
    
    # Set the plot style
    sns.set_theme(style="whitegrid")

    # Create a bar plot
    ax = sns.barplot(x='Category', y='Value', data=df)

    # Set the title of the plot
    ax.set_title('Category vs Value')

    # Display the plot
    plt.show()
    
    # Return the DataFrame and Axes
    return df, ax
