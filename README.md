#### Malicious Network Packet Classifier using AI and Python
## Introduction
This project is a simple Flask application that uses Artificial Intelligence (AI) to classify whether a message is malicious or not. The SVM model was trained on a dataset of 10,000 messages, half of which were labeled as malicious and half as benign. The dataset was preprocessed using a TF-IDF vectorizer.


## Requirements
The following packages must be installed to run the code:

- flask
- pandas
- scikit-learn

Start by installing deps

``pip install flask pandas scikit-learn``

## Run the app

``python app.py``

## Generate your own .pcap file
`` sudo tcpdump -i eth0 -n 'tcp port 80' -w file.pcap ``
