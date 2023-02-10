# Importing required libraries
import pandas as pd
import numpy as np
from sklearn.ensemble import RandomForestClassifier
import matplotlib.pyplot as plt
from scapy.all import *

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
    new_packets = [{'Length': 1000, 'Protocol': 6},
                   {'Length': 100, 'Protocol': 17}]
    new_df = pd.DataFrame(new_packets)
    predictions = clf.predict(new_df)

    # Updating the label column with the predictions
    df = pd.concat([df, pd.DataFrame([{'Time': None, 'Source': None, 'Destination': None, 'Protocol': 6, 'Length': 1000, 'Label': predictions[0]}], columns=df.columns)], ignore_index=True)
    df = pd.concat([df, pd.DataFrame([{'Time': None, 'Source': None, 'Destination': None, 'Protocol': 17, 'Length': 100, 'Label': predictions[1]}], columns=df.columns)], ignore_index=True)

    # Creating a bar chart to show the distribution of traffic by protocol
    df.groupby(['Protocol', 'Label']).sum()['Length'].unstack().plot(kind='bar', stacked=True)
    plt.show()
else:
    print("No data to fit the model")
