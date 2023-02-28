from flask import Flask
import pickle

# Initialize the Flask application
app = Flask(__name__)

# Load the model and vectorizer from the pickle files
with open('data/malicious_model.pkl', 'rb') as file:
    model = pickle.load(file)

with open('data/vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

# Import the views module
from app import views
