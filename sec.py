# Importing required libraries
import plotly.express as px
import pandas as pd
import subprocess

# Capturing live packets using Tshark
result = subprocess.Popen(['tshark', '-i', 'en0', '-T', 'fields', '-e', 'frame.time', '-e', 'ip.src', '-e', 'ip.dst', '-e', 'ip.proto', '-e', 'frame.len'], stdout=subprocess.PIPE, stderr=subprocess.PIPE)
output, errors = result.communicate()

# Converting the output of Tshark to a pandas dataframe
rows = output.splitlines()
data = [row.decode().split('\t') for row in rows]
df = pd.DataFrame(data, columns=['Time', 'Source', 'Destination', 'Protocol', 'Length'])
df = df.astype({'Length': 'int', 'Protocol': 'int'})

# Creating a bar chart to show the distribution of traffic by protocol
fig = px.bar(df, x='Protocol', y='Length', color='Protocol', title='Distribution of Traffic by Protocol')

# Showing the visualization
fig.show()
