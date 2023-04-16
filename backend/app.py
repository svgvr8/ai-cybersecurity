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
    confidence = abs(model.decision_function(input_vector)[0])

    if (prediction[0] and confidence >= 0.50) or (not prediction[0] and confidence < 0.50):
        result = 'Malicious'
    else:
        result = 'Benign'
    
    return jsonify({'result': result, 'confidence': confidence})

if __name__ == '__main__':
    app.run(debug=True)
