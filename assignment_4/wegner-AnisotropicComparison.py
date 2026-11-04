import pandas as pd
from sklearn import cluster
from sklearn import metrics
id = 200514620
df = pd.read_csv('anisotropic.csv')

kmeans_1 = cluster.KMeans(n_clusters = 3, random_state = id)
kmeans_2 = cluster.KMeans(n_clusters = 4, random_state = id)
kmeans_3 = cluster.KMeans(n_clusters = 5, random_state = id)
kmeans_1.fit(df.iloc[:, 1:])
kmeans_2.fit(df.iloc[:, 1:])
kmeans_3.fit(df.iloc[:, 1:])

agglo_1 = cluster.AgglomerativeClustering(n_clusters = 3)
agglo_2 = cluster.AgglomerativeClustering(n_clusters = 4)
agglo_3 = cluster.AgglomerativeClustering(n_clusters = 5)
agglo_1.fit(df.iloc[:, 1:])
agglo_2.fit(df.iloc[:, 1:])
agglo_3.fit(df.iloc[:, 1:])

db_1 = cluster.DBSCAN(eps = 0.1)
db_2 = cluster.DBSCAN(eps = 0.05)
db_3 = cluster.DBSCAN(eps = 0.01)
db_1.fit(df.iloc[:, 1:])
db_2.fit(df.iloc[:, 1:])
db_3.fit(df.iloc[:, 1:])

