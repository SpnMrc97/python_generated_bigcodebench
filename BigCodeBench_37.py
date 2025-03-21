from sklearn.ensemble import RandomForestClassifier
import seaborn as sns
import matplotlib.pyplot as plt
import pandas as pd
from sklearn.model_selection import train_test_split

def task_func(df, target_column):
    
    # Separate the features and the target
    X = df.drop(columns=[target_column])
    y = df[target_column]
    
    # Split the data into training and testing sets for better model evaluation
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    # Initialize the random forest classifier
    model = RandomForestClassifier(random_state=42)
    
    # Train the model
    model.fit(X_train, y_train)
    
    # Get feature importances
    importances = model.feature_importances_
    
    # Create a DataFrame for visualization
    feature_importances = pd.DataFrame({
        'Feature': X.columns,
        'Importance': importances
    }).sort_values(by='Importance', ascending=False)
    
    # Plot feature importances
    plt.figure(figsize=(10, 6))
    ax = sns.barplot(x='Importance', y='Feature', data=feature_importances, palette='viridis')
    plt.title('Visualizing Important Features')
    plt.xlabel('Feature Importance Score')
    plt.ylabel('Features')
    plt.tight_layout()
    
    # Show plot
    plt.show()
    
    return model, ax
