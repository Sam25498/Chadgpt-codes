import pandas as pd
from sklearn.cluster import KMeans

# Load the data into a pandas DataFrame
df = pd.read_csv('EURUSD_1h_20210101-20210730.csv')

# Select the relevant columns for the analysis (e.g. open, close, high, low prices)
X = df[['open', 'close', 'high', 'low']]

# Initialize the KMeans model with 3 clusters
kmeans = KMeans(n_clusters=3, random_state=0)

# Fit the model to the data
kmeans.fit(X)

# Predict the cluster labels for the data
cluster_labels = kmeans.predict(X)



