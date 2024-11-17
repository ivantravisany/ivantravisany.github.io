import streamlit as st
import seaborn as sns
import matplotlib.pyplot as plt
from sklearn.metrics import confusion_matrix, ConfusionMatrixDisplay, roc_curve, auc
from data_preparation import load_and_prepare_data
from model_training import grid_search_ann, train_and_evaluate_model
from feature_selection import select_features
import pandas as pd

# App title
st.title("Breast Cancer Analysis and Prediction")

# Load and display dataset
st.write("### Dataset Overview")
X_train, X_test, y_train, y_test = load_and_prepare_data()
st.write("Training Data Sample:")
st.write(X_train.head())

# Feature selection
X_train_selected, selected_features = select_features(X_train, y_train)
X_test_selected = X_test.iloc[:, selected_features]
st.write("### Selected Features")
st.write(list(X_train.columns[selected_features]))

# Feature Importance Visualization (Top 25)
st.write("### Feature Importance (Top 25)")
from sklearn.feature_selection import SelectKBest, f_classif
selector = SelectKBest(score_func=f_classif, k=len(X_train.columns))  # Fit on all features for scoring
selector.fit(X_train, y_train)
feature_scores = selector.scores_
selected_feature_names = X_train.columns

feature_scores_df = pd.DataFrame({
    "Feature": selected_feature_names,
    "Score": feature_scores
}).sort_values(by="Score", ascending=False).head(25)

fig, ax = plt.subplots(figsize=(10, 8))
sns.barplot(x="Score", y="Feature", data=feature_scores_df, ax=ax, palette="viridis")
ax.set_title("Top 25 Feature Importance (F-Score)")
ax.set_xlabel("F-Score")
ax.set_ylabel("Features")
st.pyplot(fig)

# Train model and evaluate
best_model = grid_search_ann(X_train_selected, y_train)
accuracy, report = train_and_evaluate_model(best_model, X_train_selected, X_test_selected, y_train, y_test)

# Create tabs for better organization
tabs = st.tabs(["Make a Prediction", "Model Training and Evaluation", "Data Visualization"])

with tabs[0]:
    st.write("### Make a Prediction")
    input_data = []
    for feature in X_train.columns[selected_features]:
        value = st.number_input(f"Enter value for {feature}:", value=0.0)
        input_data.append(value)

    if st.button("Predict"):
        prediction = best_model.predict([input_data])
        st.write(f"Prediction: {'Malignant' if prediction[0] == 1 else 'Benign'}")

with tabs[1]:
    st.write("### Model Training and Evaluation")
    st.write(f"**Test Accuracy:** {accuracy:.2f}")
    st.text("Classification Report:")
    st.text(report)

    # Confusion matrix visualization
    st.write("### Confusion Matrix")
    y_pred = best_model.predict(X_test_selected)
    cm = confusion_matrix(y_test, y_pred, labels=[0, 1])
    fig, ax = plt.subplots(figsize=(5, 5))
    ConfusionMatrixDisplay(confusion_matrix=cm, display_labels=["Benign", "Malignant"]).plot(ax=ax)
    st.pyplot(fig)

    # ROC curve visualization
    st.write("### ROC Curve")
    y_proba = best_model.predict_proba(X_test_selected)[:, 1]
    fpr, tpr, _ = roc_curve(y_test, y_proba)
    roc_auc = auc(fpr, tpr)

    fig, ax = plt.subplots(figsize=(6, 6))
    ax.plot(fpr, tpr, label=f"ROC Curve (AUC = {roc_auc:.2f})")
    ax.plot([0, 1], [0, 1], "k--", label="Random Guess")
    ax.set_xlabel("False Positive Rate")
    ax.set_ylabel("True Positive Rate")
    ax.set_title("Receiver Operating Characteristic")
    ax.legend(loc="lower right")
    st.pyplot(fig)

with tabs[2]:
    st.write("### Data Visualization")

    # Feature distribution
    st.write("#### Feature Distribution")
    feature = st.selectbox("Select a feature to visualize distribution", X_train.columns[selected_features])
    fig, ax = plt.subplots()
    sns.histplot(X_train[feature], kde=True, ax=ax)
    ax.set_title(f"Distribution of {feature}")
    st.pyplot(fig)

    # Class distribution
    st.write("#### Class Distribution")
    fig, ax = plt.subplots()
    y_train.value_counts().plot(kind="bar", color=["blue", "orange"], ax=ax)
    ax.set_title("Class Distribution (Benign vs Malignant)")
    ax.set_xticks([0, 1])
    ax.set_xticklabels(["Benign", "Malignant"], rotation=0)
    ax.set_ylabel("Count")
    st.pyplot(fig)

    # Correlation heatmap
    st.write("#### Correlation Heatmap")
    fig, ax = plt.subplots(figsize=(10, 8))
    corr = X_train.corr()
    sns.heatmap(corr, annot=False, cmap="coolwarm", ax=ax)
    ax.set_title("Feature Correlation Heatmap")
    st.pyplot(fig)

    # Scatterplot between two features
    st.write("#### Scatterplot")
    feature_x = st.selectbox("Select X-axis feature", X_train.columns[selected_features], index=0)
    feature_y = st.selectbox("Select Y-axis feature", X_train.columns[selected_features], index=1)
    fig, ax = plt.subplots()
    sns.scatterplot(x=X_train[feature_x], y=X_train[feature_y], hue=y_train, ax=ax, palette="Set2")
    ax.set_title(f"Scatterplot: {feature_x} vs {feature_y}")
    st.pyplot(fig)

    # Pairplot of selected features
    st.write("#### Pairplot of Selected Features")
    selected_data = X_train.iloc[:, selected_features].reset_index(drop=True)  # Reset index to align with y_train
    y_train_reset = y_train.reset_index(drop=True)  # Reset index for y_train
    pairplot_data = pd.concat([selected_data, y_train_reset.rename("Target")], axis=1)

    fig = sns.pairplot(pairplot_data, hue="Target", palette="Set2", diag_kind="kde", height=2)
    st.pyplot(fig)