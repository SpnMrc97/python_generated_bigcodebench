import matplotlib.pyplot as plt
import pandas as pd
import seaborn as sns
from sklearn.datasets import load_iris

def task_func():
    # Load the iris dataset
    iris = load_iris()
    iris_df = pd.DataFrame(data=iris.data, columns=iris.feature_names)
    iris_df['species'] = iris.target

    # Set font to Arial
    plt.rcParams['font.sans-serif'] = ['Arial']
    plt.rcParams['axes.unicode_minus'] = False

    # Create the pair plot
    pair_plot = sns.pairplot(iris_df, hue='species', markers=["o", "s", "D"],
                             plot_kws={'alpha': 0.5})

    # Add title
    pair_plot.fig.suptitle('Iris Dataset Pair Plot', fontsize=16)
    pair_plot.fig.subplots_adjust(top=0.95)  # Adjust the title position

    # Return the figure object
    return pair_plot.fig
