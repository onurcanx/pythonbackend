import nltk
from textblob import TextBlob
from nltk.tokenize import word_tokenize
from nltk.corpus import stopwords
import re

# NLTK gerekli dosyaları indir
nltk.download('punkt')
nltk.download('stopwords')
nltk.download('averaged_perceptron_tagger')

def clean_text(text):
    # Küçük harfe çevir
    text = text.lower()
    # Özel karakterleri kaldır
    text = re.sub(r'[^\w\s]', '', text)
    # Sayıları kaldır
    text = re.sub(r'\d+', '', text)
    return text

def remove_stopwords(text):
    stop_words = set(stopwords.words('turkish'))
    word_tokens = word_tokenize(text)
    filtered_text = [word for word in word_tokens if word not in stop_words]
    return ' '.join(filtered_text)

def analyze_comment(comment):
    try:
        # Metni temizle
        cleaned_text = clean_text(comment)
        
        # Stopwords'leri kaldır
        filtered_text = remove_stopwords(cleaned_text)
        
        # Duygu analizi
        blob = TextBlob(filtered_text)
        sentiment = blob.sentiment.polarity
        
        # Duygu durumunu belirle
        if sentiment > 0:
            sentiment_label = "Pozitif"
        elif sentiment < 0:
            sentiment_label = "Negatif"
        else:
            sentiment_label = "Nötr"
        
        # Anahtar kelimeleri çıkar
        words = word_tokenize(filtered_text)
        tagged = nltk.pos_tag(words)
        
        # Sadece isim ve sıfatları al
        keywords = [word for word, tag in tagged if tag.startswith(('NN', 'JJ'))]
        
        # Tekrar eden kelimeleri kaldır
        keywords = list(set(keywords))
        
        return {
            "sentiment": sentiment_label,
            "sentiment_score": sentiment,
            "keywords": keywords[:5],  # En önemli 5 anahtar kelime
            "original_text": comment,
            "cleaned_text": filtered_text
        }
        
    except Exception as e:
        return {
            "error": str(e),
            "sentiment": "Hata",
            "sentiment_score": 0,
            "keywords": [],
            "original_text": comment
        } 