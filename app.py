from flask import Flask, request, jsonify
from flask_cors import CORS
from nlp_analyzer import analyze_comment
import os
from dotenv import load_dotenv

load_dotenv()

app = Flask(__name__)
CORS(app)

@app.route('/api/analyze-comment', methods=['POST'])
def analyze_comment_endpoint():
    try:
        data = request.get_json()
        comment = data.get('comment')
        
        if not comment:
            return jsonify({'error': 'Yorum metni gerekli'}), 400
            
        analysis = analyze_comment(comment)
        return jsonify(analysis)
        
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/api/health', methods=['GET'])
def health_check():
    return jsonify({'status': 'healthy'})

if __name__ == '__main__':
    port = int(os.getenv('PORT', 5000))
    app.run(host='0.0.0.0', port=port) 