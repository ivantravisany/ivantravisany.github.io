# eda_and_cleaning.py
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

def load_data(file_path):
    """Load the dataset from a CSV file."""
    return pd.read_csv(file_path)

def clean_data(data):
    """Perform basic data cleaning."""
    # Drop rows with missing reviews
    data = data.dropna(subset=['review'])
    
    # Remove duplicates
    data = data.drop_duplicates(subset=['id', 'review'])
    
    # Reset index
    data = data.reset_index(drop=True)
    
    return data

def perform_eda(data):
    """Perform exploratory data analysis."""
    # Basic info
    print(data.info())
    print(data.describe())
    print(data['language'].value_counts())
    
    # Distribution of review lengths
    data['review_length'] = data['review'].str.len()
    plt.figure(figsize=(8, 6))
    sns.histplot(data['review_length'], bins=50, kde=True)
    plt.title('Distribution of Review Lengths')
    plt.xlabel('Review Length')
    plt.ylabel('Frequency')
    plt.show()
    
    # Proportion of positive vs. negative votes
    plt.figure(figsize=(8, 6))
    sns.countplot(x='voted_up', data=data)
    plt.title('Proportion of Positive and Negative Reviews')
    plt.xlabel('Voted Up')
    plt.ylabel('Count')
    plt.show()

def save_clean_data(data, output_file):
    """Save the cleaned dataset to a new CSV file."""
    data.to_csv(output_file, index=False)

def print_clean_data(data):
    """Print the cleaned dataset."""
    print(data.head())  # Print the first few rows
    print("\nData Summary:")
    print(data.info())
    print("\nMissing Values per Column:")
    print(data.isnull().sum())