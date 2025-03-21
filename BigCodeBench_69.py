import random
import matplotlib.pyplot as plt

# Constants
SALARY_RANGE = (20000, 100000)

def task_func(dict1):
    department_code = 'EMPXX'
    
    if department_code not in dict1:
        raise ValueError(f"Department {department_code} not found in the provided dictionary.")
    
    num_employees = dict1[department_code]
    
    # Generate random salaries within the specified range
    salaries = [random.randint(SALARY_RANGE[0], SALARY_RANGE[1]) for _ in range(num_employees)]
    
    # Create the histogram
    fig, ax = plt.subplots()
    ax.hist(salaries, bins=10, color='skyblue', edgecolor='black')
    
    # Set the title and labels
    ax.set_title(f'Salary Distribution in {department_code} Department')
    ax.set_xlabel('Salary')
    ax.set_ylabel('Number of Employees')
    
    # Show the plot
    plt.show()
    
    return ax
