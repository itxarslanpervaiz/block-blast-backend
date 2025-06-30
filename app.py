from flask import Flask, request, jsonify
from flask_cors import CORS
import os

app = Flask(__name__)

# ✅ Allow all origins (temporary fix)
CORS(app, resources={r"/*": {"origins": "*"}})

UPLOAD_FOLDER = './uploads'
os.makedirs(UPLOAD_FOLDER, exist_ok=True)

@app.route('/')
def index():
    return '✅ Block Blast API is running. Use POST /analyze.'

@app.route('/analyze', methods=['POST'])
def analyze_puzzle():
    if 'image' not in request.files:
        return jsonify({'error': 'No image uploaded'}), 400

    file = request.files['image']
    filepath = os.path.join(UPLOAD_FOLDER, file.filename)
    file.save(filepath)

    # Simulated output
    return jsonify({
        'total_lines_cleared': 1,
        'steps': [{'step': 'fake'}]
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
