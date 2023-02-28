from flask import Flask, render_template, request
import pickle
import pandas as pd

# Load the model and vectorizer from the pickle files
with open('data/malicious_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('data/vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

# Initialize the Flask application
app = Flask(__name__)

# Define the home page
@app.route('/')
def home():
    return render_template('index.html')

# Define the prediction function
@app.route('/predict', methods=['POST'])
def predict():
    # Get the input message from the form
    message = request.form['message']

    # Transform the input message using the vectorizer
    message_transformed = vectorizer.transform(pd.Series(message))

    # Make a prediction on the input message using the model
    prediction = model.predict(message_transformed)[0]
    proba = model.decision_function(message_transformed)[0]

    # Return the prediction and probability as a response
    return render_template('result.html', prediction=prediction, proba=proba)

# Start the Flask application
if __name__ == '__main__':
    app.run(debug=True)