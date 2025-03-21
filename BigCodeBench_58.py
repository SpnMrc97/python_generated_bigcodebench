import numpy as np
from scipy import stats
import matplotlib.pyplot as plt

def task_func(mu, sigma, num_samples):
    # Generate random samples from a normal distribution
    samples = np.random.normal(mu, sigma, num_samples)

    # Create a range of x values for the theoretical normal distribution
    x = np.linspace(mu - 4*sigma, mu + 4*sigma, 1000)
    # Calculate the corresponding y values for the normal distribution
    y = stats.norm.pdf(x, mu, sigma)

    # Create the plot
    fig, ax = plt.subplots(figsize=(8, 6))
    
    # Plot the histogram of the samples
    ax.hist(samples, bins=30, density=True, alpha=0.6, color='g', label='Sample Histogram')
    
    # Plot the theoretical normal distribution
    ax.plot(x, y, 'r-', lw=2, label='Normal Distribution (PDF)')
    
    # Set the title and labels
    ax.set_title('Normal Distribution')
    ax.set_xlabel('Value')
    ax.set_ylabel('Probability Density')
    
    # Add a legend
    ax.legend()

    # Show the plot
    plt.show()
    
    return fig
