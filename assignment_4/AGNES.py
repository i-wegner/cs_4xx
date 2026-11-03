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
        row = x[0]
        col = x[1]

        D[D.iloc[x[:2]] == abs_min] = 0.00

        value_one = x[0]
        value_two = int(x[1])
        key_one = next((k for k, v in K.items() if v == value_one), None)
        key_two = next((k for k, v in K.items() if v == value_two), None)

        K.update({c : [K[key_one], K[key_two]]})
        del K[key_one], K[key_two]
        c = c + 1

    return K

K = AGNES(df)
print(K)
print(df)

# breaks when multiple minimum instances occur