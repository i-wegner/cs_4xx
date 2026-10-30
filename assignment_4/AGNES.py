import pandas as pd
import numpy as np

df = pd.read_csv('Q1-pairwise-distances.csv')
df = df.drop(columns = ['Instance'])

def minDistance(df):
    min_distance_series = df[df > 0].min() # returns pandas series with min distance in each column
    abs_min_distance = df[df > 0].min().min() # returns the absolute min, must be equivalent in at least 2 indices
    x, y = np.where(df == abs_min_distance)
    """ z = []
    for i in range(len(x)):
        z.append(x[i]) """
    return abs_min_distance, x


def AGNES(D):
    K = {}
    # instatiate initial sets K_1, ... , K_n
    for i in range(len(D)):
        K[i] = set()
        K[i].add(i)
    c = len(K) + 1


    while len(K) > 1:
        abs_min, x = minDistance(D)

        D[D.iloc[x] == abs_min] = 0.00
        K.update({c : [K[x[0]], K[x[1]]]})
        del K[x[0]], K[x[1]]
        c = c + 1

    return K

K = AGNES(df)
print(K)
print(df)