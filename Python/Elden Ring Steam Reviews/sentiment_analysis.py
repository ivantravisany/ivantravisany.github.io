# sentiment_analysis.py
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer
from transformers import pipeline

# Download VADER lexicon
nltk.download('vader_lexicon')

def analyze_sentiment_vader(text):
    analyzer = SentimentIntensityAnalyzer()
    score = analyzer.polarity_scores(text)
    if score['compound'] > 0.05:
        return 'positive'
    elif score['compound'] < -0.05:
        return 'negative'
    else:
        return 'neutral'

def analyze_sentiment_transformers(text):
    classifier = pipeline("sentiment-analysis")
    result = classifier(text)[0]['label']
    return result.lower()  # Convert to lowercase to match consistency