# app.py
from flask import Flask, request, jsonify, send_file
import os
import time
import multiprocessing
import numpy as np
from io import BytesIO
from prometheus_client import Counter, generate_latest, CONTENT_TYPE_LATEST

app = Flask(__name__)

REQUEST_COUNT = Counter('photo_microservice_requests_total', 'Total number of requests', ['method', 'endpoint'])

@app.route('/')
def index():
    REQUEST_COUNT.labels(method='GET', endpoint='/').inc()
    return 'Hello from photo-microservice!'

@app.route('/process-photo', methods=['POST'])
def process_photo():
    REQUEST_COUNT.labels(method='POST', endpoint='/process-photo').inc()
    if 'file' not in request.files:
        return jsonify({'error': 'No file part in the request'}), 400
    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400
    
    # Simulate GPU processing by performing CPU-intensive computations
    try:
        start_time = time.time()
        data = file.read()
        
        size = 500
        matrix_a = np.random.rand(size, size)
        matrix_b = np.random.rand(size, size)
        result = np.dot(matrix_a, matrix_b)
        
        processing_time = time.time() - start_time
        return jsonify({
            'message': f'Processed photo {file.filename} in {processing_time:.2f} seconds'
        }), 200
    except Exception as e:
        return jsonify({'error': str(e)}), 500

@app.route('/metrics')
def metrics():
    return generate_latest(), 200, {'Content-Type': CONTENT_TYPE_LATEST}

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=80)
