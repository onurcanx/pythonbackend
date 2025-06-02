import nltk
from nltk.sentiment import SentimentIntensityAnalyzer
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import string
import re

# NLTK verilerini indir
try:
    nltk.data.find('tokenizers/punkt')
except LookupError:
    nltk.download('punkt')

try:
    nltk.data.find('sentiment/vader_lexicon.zip')
except LookupError:
    nltk.download('vader_lexicon')

try:
    nltk.data.find('corpora/stopwords')
except LookupError:
    nltk.download('stopwords')

def clean_text(text):
    # Küçük harfe çevir
    text = text.lower()
    
    # Noktalama işaretlerini kaldır
    text = text.translate(str.maketrans('', '', string.punctuation))
    
    # Sayıları kaldır
    text = re.sub(r'\d+', '', text)
    
    # Fazla boşlukları temizle
    text = ' '.join(text.split())
    
    return text

def get_keywords(text, max_keywords=5):
    # Metni tokenize et
    tokens = word_tokenize(text)
    
    # Stopwords'leri kaldır
    stop_words = set(stopwords.words('turkish'))
    tokens = [word for word in tokens if word not in stop_words]
    
    # Kelime frekanslarını hesapla
    word_freq = {}
    for word in tokens:
        if word in word_freq:
            word_freq[word] += 1
        else:
            word_freq[word] = 1
    
    # En sık kullanılan kelimeleri al
    keywords = sorted(word_freq.items(), key=lambda x: x[1], reverse=True)
    return [word for word, freq in keywords[:max_keywords]]

def analyze_text(text):
    # Metni temizle
    cleaned_text = clean_text(text)
    
    # Duygu analizi yap
    sia = SentimentIntensityAnalyzer()
    sentiment_scores = sia.polarity_scores(cleaned_text)
    
    # Duygu durumunu belirle
    compound_score = sentiment_scores['compound']
    if compound_score >= 0.05:
        sentiment = 'positive'
    elif compound_score <= -0.05:
        sentiment = 'negative'
    else:
        sentiment = 'neutral'
    
    # Anahtar kelimeleri çıkar
    keywords = get_keywords(cleaned_text)
    
    return {
        'sentiment': sentiment,
        'sentiment_score': compound_score,
        'keywords': keywords
    } 