from flask import Flask, request, jsonify
from flask_cors import CORS
import pandas as pd
import pickle
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC

app = Flask(__name__)
CORS(app)

with open('data/vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

with open('data/malicious_model.pkl', 'rb') as file:
    model = pickle.load(file)

@app.route('/classify', methods=['POST'])
def classify():
    text = request.json['text']
    input_vector = vectorizer.transform([text])
    prediction = model.predict(input_vector)
    result = 'Malicious' if prediction[0] else 'Benign'
    return jsonify({'result': result})

if __name__ == '__main__':
    app.run(debug=True)

