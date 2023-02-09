#### Network Traffic Analysis using AI and Python
## Introduction
This project aims to analyze network traffic for potential threats by using AI and Python. It uses the Scapy library to capture network packets and the Pandas library to convert the packets into a dataframe. The dataframe is then analyzed using a random forest classifier to predict if a packet is malicious or not based on its length and protocol. The results of the analysis are visualized using Plotly.

## Requirements
The following packages must be installed to run the code:

- scapy
- pandas
- plotly
- scikit-learn