# Importing required libraries
from scapy.all import *
import pandas as pd

# Reading the PCAP file
packets = rdpcap('sample.pcap')

# Converting the packets to a pandas dataframe
df = pd.DataFrame(columns=['Time', 'Source', 'Destination', 'Protocol', 'Length'])
for packet in packets:
    row = {'Time': packet.time, 'Source': packet[IP].src, 'Destination': packet[IP].dst, 'Protocol': packet[IP].proto, 'Length': len(packet)}
    df = df.append(row, ignore_index=True)

# Implementing your AI algorithms here to analyze the data for potential threats
# ...

# Displaying the results
print(df)
