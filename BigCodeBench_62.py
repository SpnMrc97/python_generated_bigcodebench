import random
import matplotlib.pyplot as plt
import seaborn as sns

def task_func(result, colors=['b', 'g', 'r', 'c', 'm', 'y', 'k']):
    # Extract the 'from_user' values from the list of dictionaries
    from_user_values = [entry['from_user'] for entry in result if 'from_user' in entry]

    # Randomly select a color for the histogram bars
    bar_color = random.choice(colors)

    # Set up the seaborn style
    sns.set(style="whitegrid")

    # Create the histogram
    plt.hist(from_user_values, bins=10, color=bar_color, edgecolor='black')

    # Add labels and title
    plt.xlabel('Value of from_user')
    plt.ylabel('Frequency')
    plt.title('Histogram of from_user values')

    # Display the histogram
    plt.show()
