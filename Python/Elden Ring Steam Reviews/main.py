# main.py
import eda_and_cleaning as eda
import sentiment_analysis as sa

# Load dataset
data = eda.load_data('/Users/ivantravisany/Documents/Estudios/git/ivantravisany.github.io/Python/Elden Ring Steam Reviews/elden_ring_steam_reviews.csv')

# Perform EDA, clean data and print
eda.perform_eda(data)
data = eda.clean_data(data)
eda.print_clean_data(data)

# Perform sentiment analysis
data['sentiment'] = data['review'].apply(sa.analyze_sentiment_vader)

# Save the final dataset
eda.save_clean_data(data, '/Users/ivantravisany/Documents/Estudios/git/ivantravisany.github.io/Python/Elden Ring Steam Reviews/data_with_sentiment.csv')

print("Process completed. Data saved to 'steam_reviews_with_sentiment.csv'.")