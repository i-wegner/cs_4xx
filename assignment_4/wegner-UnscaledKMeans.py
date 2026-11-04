import pandas as pd
import numpy as np
from sklearn import cluster
from matplotlib import pyplot as plt
id = 200514620

df = pd.read_csv('different_scales.csv')
# copies of df so that df is unchanged when we normalize/standardize
df2 = df.copy()
df3 = df.copy()

def normalize_variable(df): # normalize linear attributes(s)
    # more general approach than used in Q2
    attributes = df.columns.tolist() # instatiate list of column names from df
    for attribute in attributes:
        s_min = df[attribute].min()
        s_max = df[attribute].max()

        if s_min == s_max:
            return df[attribute] * 0

        else:
            df[attribute] = (df[attribute] - s_min) / (s_max - s_min)

def standardize_variable(df):
    n = len(df)
    attributes = df.columns.tolist()
    ave = df.mean()
    std = df.std() # pandas std() default ddof = 1 for sample std
    

    for attribute in attributes:
        df[attribute] = (df[attribute] - ave[attribute]) / std[attribute]

normalize_variable(df2)
standardize_variable(df3)

km_cluster1 = cluster.KMeans(n_clusters = 3, random_state = id)
km_cluster2 = cluster.KMeans(n_clusters = 3, random_state = id)
km_cluster3 = cluster.KMeans(n_clusters = 3, random_state = id)

km_cluster1.fit(df)
km_cluster2.fit(df2)
km_cluster3.fit(df3)

fig1 = plt.figure()
ax = fig1.add_subplot(projection = "3d")
ax.scatter(df.iloc[:, 0], df.iloc[:, 1],
           df.iloc[:, 2], c = km_cluster1.labels_)
plt.savefig('Wegner-Kmeans-unscaled.png')

fig2 = plt.figure()
ax = fig2.add_subplot(projection = "3d")
ax.scatter(df2.iloc[:, 0], df2.iloc[:, 1],
           df2.iloc[:, 2], c = km_cluster2.labels_)
plt.savefig('Wegner-KMeans-normalized.png')

fig3 = plt.figure()
ax = fig3.add_subplot(projection = "3d")
ax.scatter(df3.iloc[:, 0], df3.iloc[:, 1],
           df3.iloc[:, 2], c = km_cluster3.labels_)
plt.savefig('Wegner-KMeans-standardized.png')
