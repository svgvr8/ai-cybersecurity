# Importing required libraries
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from scapy.all import *
from scapy.layers.inet import IP


# Loading the pcap file using Scapy
packets = rdpcap("file.pcap")

# Converting the Scapy packets into a pandas dataframe
df = pd.DataFrame(columns=['Time', 'Source', 'Destination', 'Protocol', 'Length'])
for packet in packets:
    df = df.append({'Time': packet.time, 'Source': packet[IP].src, 'Destination': packet[IP].dst, 'Protocol': packet[IP].proto, 'Length': len(packet)}, ignore_index=True)

# Adding a label column to the dataframe
df['Label'] = np.zeros(df.shape[0])

# Check if the dataframe is not empty
if df.shape[0] > 0:
    # Implementing your AI algorithms here to analyze the data for potential threats
    # ...
    # For example, training a random forest classifier to predict if a packet is malicious or not
    X = df[['Length', 'Protocol']]
    y = df['Label']
    clf = RandomForestClassifier()
    clf.fit(X, y)
    
    # Predicting the labels for new packets
    predictions = clf.predict(X)
    
    # Updating the label column with the predictions
    df['Label'] = predictions

    # Creating a bar chart to show the distribution of traffic by protocol
    df.groupby(['Protocol', 'Label']).sum()['Length'].unstack().plot(kind='bar', stacked=True)
    
    # Adding labels to the graph
    plt.xlabel("Network Protocol (UDP, TCP)")
    plt.ylabel("Bytes")
    plt.title("Distribution of Traffic by Network Protocol (UDP, TCP) and Maliciousness")
    
    plt.show()
else:
    print("No data to fit the model")
