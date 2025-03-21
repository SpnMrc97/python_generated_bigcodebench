import wikipedia
from wordcloud import WordCloud
import matplotlib.pyplot as plt

def task_func(page_title):
    try:
        # Fetch Wikipedia page content
        page_content = wikipedia.page(page_title).content
        
        # Generate word cloud
        wordcloud = WordCloud(width=800, height=400, background_color='white').generate(page_content)
        
        # Plot the word cloud
        plt.figure(figsize=(10, 5))
        ax = plt.imshow(wordcloud, interpolation='bilinear')
        plt.axis('off')
        plt.show()

        return ax
    except wikipedia.exceptions.PageError:
        print(f"No Wikipedia page found for title: {page_title}")
        return None
    except wikipedia.exceptions.DisambiguationError as e:
        print(f"Disambiguation error for title: {page_title}. Suggestions: {e.options}")
        return None
