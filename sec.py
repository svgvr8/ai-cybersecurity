# Importing required libraries
import plotly.express as px
import pandas as pd
import subprocess
import numpy as np
from sklearn.ensemble import RandomForestClassifier

# Capturing live packets using Tshark
result = subprocess.Popen(['tshark', '-i', 'eth0', '-T', 'fields', '-e', 'frame.time', '-e', 'ip.src', '-e', 'ip.dst', '-e', 'ip.proto', '-e', 'frame.len'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, errors = result.communicate()

print(output) # Add this line to check the output of the Tshark command

# Converting the output of Tshark to a pandas dataframe
rows = output.splitlines()
data = [row.decode().split('\t') for row in rows]
df = pd.DataFrame(data, columns=['Time', 'Source', 'Destination', 'Protocol', 'Length'])
df = df.astype({'Length': 'int', 'Protocol': 'int'})

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
    df.loc[df.shape[0]] = [None, None, None, None, 1000, 6, predictions[0]]
    df.loc[df.shape[0]] = [None, None, None, None, 100, 17, predictions[1]]

    # Creating a bar chart to show the distribution of traffic by protocol
    fig = px.bar(df, x='Protocol', y='Length', color='Label', title='Distribution of Traffic by Protocol and Threat Level')

    # Showing the visualization
    fig.show()
else:
    print("No data to fit the model")
