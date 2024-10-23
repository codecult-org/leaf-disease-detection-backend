from flask import Flask, request, jsonify
import function
import json
import os
from flask_cors import CORS

app = Flask(__name__)
CORS(app, origins=[
    '*'
])

# @app.after_request
# def add_cors_headers(response):
#     response.headers['Access-Control-Allow-Origin'] = 'https://leaf-disease-detection-ecru.vercel.app/'
#     response.headers['Access-Control-Allow-Headers'] = 'Content-Type'
#     response.headers['Access-Control-Allow-Methods'] = 'POST'
#     return response


@app.route('/')
def hello():
    return 'Welcome to leaf disease detection!'


@app.route('/checking', methods=['POST'])
def sup():
    file_path = ''
    if 'file' not in request.files:
        return jsonify({'error': 'No file part'}), 400

    file = request.files['file']
    if file.filename == '':
        return jsonify({'error': 'No selected file'}), 400

    if file:
        file_path = os.path.join('./image', file.filename)
        print("# image path: "+file_path)  # for testing
        file.save(file_path)

    data = function.evaluate(file_path)
    json_data = json.dumps(data)
    print('# result: ', data)  # for testing
    return json_data
