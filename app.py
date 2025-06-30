from flask import Flask, request, jsonify
from flask_cors import CORS
import os
from solver import solve_puzzle
from grid_detector import extract_grid

app = Flask(__name__)
CORS(app, origins=["https://thailandcapcuttemplate.arslanpervaiz.me"])

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

    grid = extract_grid(filepath)
    steps, total_lines = solve_puzzle(grid)

    return jsonify({
        'total_lines_cleared': total_lines,
        'steps': steps
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=10000)
