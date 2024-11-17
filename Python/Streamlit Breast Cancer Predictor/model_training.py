from sklearn.neural_network import MLPClassifier
from sklearn.model_selection import GridSearchCV
from sklearn.metrics import classification_report, accuracy_score

# Grid Search CV for hyperparameter tuning
def grid_search_ann(X_train, y_train):
    param_grid = {
        'hidden_layer_sizes': [(50, 50), (100,), (100, 50)],
        'activation': ['relu', 'tanh'],
        'solver': ['adam', 'sgd'],
        'max_iter': [200, 500]
    }
    model = MLPClassifier(random_state=42)
    grid_search = GridSearchCV(model, param_grid, cv=3, scoring='accuracy', n_jobs=-1)
    grid_search.fit(X_train, y_train)
    return grid_search.best_estimator_

# Train and evaluate the model
def train_and_evaluate_model(model, X_train, X_test, y_train, y_test):
    # Train the model
    model.fit(X_train, y_train)
    
    # Make predictions
    y_pred = model.predict(X_test)
    
    # Evaluate the model
    accuracy = accuracy_score(y_test, y_pred)
    report = classification_report(y_test, y_pred, target_names=["Benign", "Malignant"])
    
    # Return both accuracy and report
    return accuracy, report

if __name__ == "__main__":
    from data_preparation import load_and_prepare_data
    from feature_selection import select_features

    # Load and preprocess the dataset
    X_train, X_test, y_train, y_test = load_and_prepare_data()
    X_train_selected, selected_features = select_features(X_train, y_train)
    X_test_selected = X_test.iloc[:, selected_features]

    # Grid Search for best model
    best_model = grid_search_ann(X_train_selected, y_train)

    # Train and evaluate the best model
    accuracy, report = train_and_evaluate_model(best_model, X_train_selected, X_test_selected, y_train, y_test)
    print(f"Test Accuracy: {accuracy:.2f}")
    print("Classification Report:")
    print(report)