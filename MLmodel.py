import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn.feature_extraction.text import TfidfVectorizer
from sklearn.svm import LinearSVC
from sklearn.metrics import accuracy_score
import pickle

# Load the dataset
data = pd.read_csv("data/malicious.csv")

# Split the dataset into train and test sets
train_data, test_data = train_test_split(data, test_size=0.2, random_state=42)

# Create the vectorizer
vectorizer = TfidfVectorizer()

# Fit the vectorizer on the training data
vectorizer.fit(train_data['info'])

# Save the vectorizer as a pickle file
with open('data/vectorizer.pkl', 'wb') as file:
    pickle.dump(vectorizer, file)

# Transform the training and test data
X_train = vectorizer.transform(train_data['info'])
y_train = train_data['malicious']
X_test = vectorizer.transform(test_data['info'])
y_test = test_data['malicious']

# Create the model
model = LinearSVC()

# Train the model
model.fit(X_train, y_train)

# Predict on the test data
y_pred = model.predict(X_test)

# Save the model as a pickle file
with open('data/malicious_model.pkl', 'wb') as file:
    pickle.dump(model, file)

# Evaluate the model and print in percentage
accuracy = accuracy_score(y_test, y_pred)
print("Accuracy on the above dataset: {:.0f}%".format(accuracy * 100))