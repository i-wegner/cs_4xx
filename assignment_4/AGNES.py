import pandas as pd
import numpy as np

df = pd.read_csv('Q1-pairwise-distances.csv')
df = df.drop(columns = ['Instance'])

def minDistance(df):
    min_distance_series = df[df > 0].min() # returns pandas series with min distance in each column
    abs_min_distance = df[df > 0].min().min() # returns the absolute min, must be equivalent in at least 2 indices
    x, y = np.where(df.to_numpy() == abs_min_distance)
    z = []
    for i in range(len(x)):
        z.append([x[i], y[i]])
    return z 

z = minDistance(df)
print(z[0][0])


def AGNES(D):
    K = {}
    for i in range(1, len(D) + 1):
        K[i] = set()
    #print(K)

AGNES(df)