# Film Yorum Analizi - Python Backend

Bu proje, film yorumlarını analiz eden ve kullanıcıların film deneyimlerini paylaşabilecekleri web uygulamasının Python backend kısmıdır.

## Özellikler

- NLP tabanlı yorum analizi
- Duygu analizi
- Anahtar kelime çıkarma
- RESTful API endpoints

## Teknolojiler

- Python
- Flask
- SQLAlchemy
- NLTK
- TextBlob

## Kurulum

1. Python sanal ortamı oluşturun:
```bash
python -m venv venv
source venv/bin/activate  # Linux/Mac
venv\Scripts\activate     # Windows
```

2. Gerekli paketleri yükleyin:
```bash
pip install -r requirements.txt
```

3. Veritabanını oluşturun:
```bash
python init_db.py
```

4. Sunucuyu başlatın:
```bash
python app.py
```

## API Endpoints

### Yorum Analizi
- `POST /api/analyze-comment`
  - Yorum metnini analiz eder
  - Duygu analizi ve anahtar kelimeleri döndürür

### Film Bilgileri
- `GET /api/movies`
  - Film listesini döndürür
- `GET /api/movies/<id>`
  - Belirli bir filmin detaylarını döndürür

## Çevre Değişkenleri

`.env` dosyasında aşağıdaki değişkenleri tanımlayın:
```
DATABASE_URL=postgresql://user:password@localhost:5432/dbname
NODE_BACKEND_URL=http://localhost:3001
```

## Lisans

MIT 