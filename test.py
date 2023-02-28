import pickle

# Load the model from the pickle file
with open('malicious_model.pkl', 'rb') as file:
    model = pickle.load(file)

# Define some new text data to classify
new_data = ['This is a normal message.', 'Standard query 0xa002 A abc23.malware.com']

# Load the vectorizer from the pickle file
with open('vectorizer.pkl', 'rb') as file:
    vectorizer = pickle.load(file)

# Transform the new data using the same vectorizer used during training
new_data_transformed = vectorizer.transform(new_data)

# Make predictions on the new data using the trained model
predictions = model.predict(new_data_transformed)

# Print the predicted classes and probabilities
print("Predicted Classes:", predictions)
probs = model._predict_proba_lr(new_data_transformed)
print("Class Probabilities:", probs)
