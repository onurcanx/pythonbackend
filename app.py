from flask import Flask, request, jsonify
from flask_cors import CORS
from nlp_analyzer import analyze_text
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)

# CORS ayarları
cors = CORS(app, resources={
    r"/*": {
        "origins": [os.getenv('FRONTEND_URL', 'http://localhost:3000')],
        "methods": ["GET", "POST", "OPTIONS"],
        "allow_headers": ["Content-Type", "Authorization"]
    }
})

@app.route('/analyze', methods=['POST'])
def analyze():
    try:
        data = request.get_json()
        text = data.get('text', '')

        if not text:
            return jsonify({'error': 'Metin boş olamaz'}), 400

        result = analyze_text(text)
        return jsonify(result)

    except Exception as e:
        print(f"Analiz hatası: {str(e)}")
        return jsonify({'error': 'Sunucu hatası'}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 