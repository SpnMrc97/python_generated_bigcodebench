import re
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def task_func(text):

    # Remove URLs using regex
    text_without_urls = re.sub(r'http[s]?://\S+', '', text)

    # Check if there's any words left after removing URLs
    if not text_without_urls.strip():
        raise ValueError("No words available to generate a word cloud after removing URLs.")

    # Generate the word cloud
    wordcloud = WordCloud(width=800, height=400, background_color='white').generate(text_without_urls)

    # Plot the word cloud
    plt.figure(figsize=(10, 5))
    plt.imshow(wordcloud, interpolation='bilinear')
    plt.axis('off')
    plt.show()

    return wordcloud
