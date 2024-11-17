from sklearn.datasets import load_breast_cancer
import pandas as pd
from sklearn.model_selection import train_test_split

def load_and_prepare_data():
    # Load dataset
    data = load_breast_cancer()
    X = pd.DataFrame(data.data, columns=data.feature_names)
    y = pd.Series(data.target, name="target")
    
    # Split data
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    
    return X_train, X_test, y_train, y_test

if __name__ == "__main__":
    X_train, X_test, y_train, y_test = load_and_prepare_data()
    print("Data loaded and split successfully!")