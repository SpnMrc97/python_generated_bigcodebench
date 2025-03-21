import json
import pandas as pd

def task_func(result, csv_file_path="test.csv", json_file_path="test.json"):
    
    # Convert the list of dictionaries to a DataFrame
    df = pd.DataFrame(result)
    
    # Save the DataFrame to a CSV file without index
    df.to_csv(csv_file_path, index=False)
    
    # Save the list of dictionaries to a JSON file
    with open(json_file_path, 'w') as json_file:
        json.dump(result, json_file, indent=4)

# Example usage
if __name__ == "__main__":
    result = [{"hi": 7, "bye": 4, "from_user": 0}, {1: 2, 3: 4, 5: 6}]
    task_func(result, 'test.csv', 'test.json')
