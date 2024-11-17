from sklearn.feature_selection import SelectKBest, f_classif

def select_features(X_train, y_train, k=10):
    selector = SelectKBest(score_func=f_classif, k=k)
    X_train_selected = selector.fit_transform(X_train, y_train)
    selected_features = selector.get_support(indices=True)
    return X_train_selected, selected_features

if __name__ == "__main__":
    from data_preparation import load_and_prepare_data
    X_train, _, y_train, _ = load_and_prepare_data()
    X_train_selected, selected_features = select_features(X_train, y_train)
    print("Selected features:", selected_features)