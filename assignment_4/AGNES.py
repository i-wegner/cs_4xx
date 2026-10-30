import pandas as pd
import numpy as np

df = pd.read_csv('Q1-pairwise-distances.csv')
df = df.drop(columns = ['Instance'])

def minDistance(df):
    min_distance_series = df[df > 0].min() # returns pandas series with min distance in each column
    abs_min_distance = df[df > 0].min().min() # returns the absolute min, must be equivalent in at least 2 indices
    x, y = np.where(df.to_numpy() == abs_min_distance)
    """ z = []
    for i in range(len(x)):
        z.append(x[i]) """
    return x, y


def AGNES(D):
    K = {}
    # instatiate initial sets K_1, ... , K_n
    for i in range(1, len(D) + 1):
        K[i] = set()
        K[i].add(i)

    min_distance_list = minDistance(D)
    x, y= min_distance_list.pop(0), min_distance_list.pop(0)
    print(x,y)

    """ while len(K) > 1:
        for i in range(2):
            D[D.iloc[]] """
    return K

K = AGNES(df)
print(K)
print(df)