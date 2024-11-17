# Breast Cancer Analysis and Prediction

## Overview
This project provides a comprehensive analysis of the Breast Cancer dataset using feature selection, an Artificial Neural Network (ANN) model, and hyperparameter tuning via Grid Search Cross-Validation. It also includes a **Streamlit app** for interactive exploration of the dataset, model evaluation, and predictions.

The app incorporates:
- Dataset overview and feature visualization.
- Interactive model evaluation metrics like **confusion matrix**, **ROC curve**, and **classification report**.
- User-friendly prediction interface for predicting if a tumor is **malignant** or **benign**.

---

## **Features**
1. **Dataset Overview**:
   - Display the structure and sample data from the Breast Cancer dataset.
2. **Feature Selection**:
   - Perform feature selection using the `SelectKBest` method to retain the most relevant features.
3. **Feature Importance Visualization**:
   - Visualize the top 25 features based on their F-scores.
4. **Model Training and Evaluation**:
   - Train an Artificial Neural Network (ANN) using `MLPClassifier`.
   - Optimize hyperparameters with Grid Search Cross-Validation.
   - Evaluate the model with accuracy, confusion matrix, classification report, and ROC curve.
5. **Interactive Tabs**:
   - **Make a Prediction**: Input feature values and predict whether a tumor is malignant or benign.
   - **Model Evaluation**: View detailed model performance metrics and visualizations.
   - **Data Visualization**: Explore feature distributions, class distributions, scatterplots, and correlation heatmaps.
6. **Interactive Visualizations**:
   - Feature distributions.
   - Correlation heatmap.
   - Class distribution bar chart.
   - Pairwise scatterplots with color-coded classes.

---

## How to Use

### Prerequisites
1. Install Python (>=3.7) and Set Up a Virtual Environment
    ```bash
    python3 -m venv .venv
    source .venv/bin/activate  # macOS/Linux
    .venv\Scripts\activate     # Windows

2. Install required libraries using:
   ```bash
   pip install -r requirements.txt

3. Run the Streamlit app:
    ```bash
    streamlit run app.py

4. Open the app in your browser at http://localhost:8501

---

## **App Structure**

### **Dataset Overview**
- Displays the dataset structure and a sample of the training data.

### **Feature Selection**
- Highlights the selected features used for model training.

### **Feature Importance Visualization**
- A bar chart of the top 25 features based on F-scores.

### **Interactive Tabs**
1. **Make a Prediction**:
   - Enter values for the selected features.
   - Predict whether the tumor is benign or malignant.
2. **Model Evaluation**:
   - View key metrics such as accuracy, precision, recall, and F1-score.
   - Visualize the confusion matrix and ROC curve.
3. **Data Visualization**:
   - Explore the data with the following visualizations:
     - **Feature Distributions**: Select a feature and view its distribution.
     - **Class Distribution**: View the distribution of benign and malignant cases.
     - **Correlation Heatmap**: Understand relationships between features.
     - **Scatterplots**: Explore relationships between two selected features.
     - **Pairplot**: Visualize pairwise relationships for selected features.

---

## **Model Performance**

### **Metrics**
- **Accuracy**: 96%
- **Precision**:
  - Benign: 0.95
  - Malignant: 0.97
- **Recall**:
  - Benign: 0.95
  - Malignant: 0.97
- **F1-Score**:
  - Benign: 0.95
  - Malignant: 0.97

### **Confusion Matrix**
| Actual \ Predicted | Benign | Malignant |
|---------------------|--------|-----------|
| **Benign**          | 41     | 2         |
| **Malignant**       | 2      | 69        |

### **ROC Curve**
The ROC curve demonstrates high performance, with an Area Under the Curve (AUC) of 0.98.

---

## **File Structure**
- `data_preparation.py`: Loads and splits the dataset into training and test sets.
- `feature_selection.py`: Selects the most relevant features using `SelectKBest`.
- `model_training.py`: Defines and trains the ANN model with hyperparameter tuning.
- `app.py`: Streamlit app that integrates data analysis, model training, evaluation, and interactive predictions.
- `requirements.txt`: List of Python dependencies.

---

## **Future Improvements**
- Add SHAP or LIME explainability tools to make predictions more interpretable.
- Test the model on external datasets to evaluate its generalizability.
- Deploy the app to the cloud for public access.

---

## **Acknowledgments**
- Dataset source: UCI Machine Learning Repository.
- Frameworks used: Scikit-learn, Streamlit, Matplotlib, Seaborn, Pandas.

---

## **Contributing**
Contributions are welcome! Please fork the repository and submit a pull request for improvements or bug fixes.