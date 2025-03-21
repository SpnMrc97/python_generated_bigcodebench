import csv
import collections
import operator

def task_func(csv_file_path):
    # Use a defaultdict to accumulate quantities for each product
    sales_counter = collections.defaultdict(int)
    
    # Open and read the CSV file
    with open(csv_file_path, mode='r', newline='') as file:
        reader = csv.DictReader(file)
        
        # Iterate through each row in the CSV
        for row in reader:
            product = row['product']
            quantity = int(row['quantity'])
            # Accumulate the quantities for each product
            sales_counter[product] += quantity
    
    # Determine the product with the highest total quantity sold
    best_selling_product = max(sales_counter.items(), key=operator.itemgetter(1))[0]
    
    return best_selling_product
