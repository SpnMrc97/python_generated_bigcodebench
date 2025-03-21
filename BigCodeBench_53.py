import pandas as pd
import regex as re
import seaborn as sns
import matplotlib.pyplot as plt

COLUMN_NAMES = ["Name", "Email", "Age", "Country"]

def task_func(text):
    # Define the regular expression pattern
    pattern = r"Name: (.*?), Email: (.*?), Age: (.*?), Country: (.*?)($|\n)"
    
    # Find all matches using the pattern
    matches = re.findall(pattern, text)
    
    # Create a list of dictionaries, each containing the extracted data
    data = []
    for match in matches:
        data.append({
            "Name": match[0],
            "Email": match[1],
            "Age": int(match[2]),  # Convert age to integer
            "Country": match[3]
        })
    
    # Create a DataFrame from the list of dictionaries
    df = pd.DataFrame(data, columns=COLUMN_NAMES)
    
    # Plot the age distribution using seaborn
    sns.histplot(df['Age'], kde=True)
    plt.title('Age Distribution')
    plt.xlabel('Age')
    plt.ylabel('Frequency')
    plt.show()
    
    return df
