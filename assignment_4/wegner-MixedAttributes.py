import numpy as np
import pandas as pd

df = pd.read_csv('mixed_data.csv')

def normalize_variable(series): # normalize linear attributes(s)
    s_min = series.min()
    s_max = series.max()

    if s_min == s_max:
        return series * 0

    else:
        series = (series - s_min) / (s_max - s_min)

    return series

def rank_transform(series): # rank transformation and normilization for nonlinear attribute(s)
    series = series.rank(method = 'dense')
    s_min = series.min()
    s_max = series.max()

    if s_min == s_max:
        return series * 0

    else:
        series = (series - s_min) / (s_max - s_min)

    return series

df['MedianWage'] = normalize_variable(df['MedianWage'])
df['Ranking'] = normalize_variable(df['Ranking'])
df['NumberOfEmployees'] = rank_transform(df['NumberOfEmployees'])

attribute_types = ['linear',
                   'ordinal',
                   'nonlinear',
                   'asymmetric binary',
                   'nominal']

def mixed_dissimilarity(object1, object2, attribute_types):
    numerator = 0
    distance = []
    delta = []
    for i, item in enumerate(attribute_types):
        if item in ['linear', 'ordinal', 'nonlinear']:
            distance.append(np.abs(object1.iloc[i] - object2.iloc[i]))
            delta.append(1)

        elif item == 'nominal':
            if object1.iloc[i] != object2.iloc[i]:
                distance.append(1)
            else:
                distance.append(0)
            delta.append(1)

        elif item == 'symmetric binary':
            if object1.iloc[i] != object2.iloc[i]:
                distance.append(1)
            else:
                distance.append(0)
            delta.append(1)

        elif item == 'asymmetric binary':
            if object1.iloc[i] == 0 and object2.iloc[i] == 0:
                distance.append(0)
                delta.append(0)
            else:
                distance.append(1)
                delta.append(1)

        numerator += delta[i] * distance[i]

    denominator = sum(delta)
    object_distance = numerator / denominator

    return object_distance

def dissimilarityMatrix(df):
    n = len(df)
    dissimilarity_matrix = pd.DataFrame(np.zeros((n, n)))
    for i in range(n):
        for j in range(i + 1, n):
            object1 = df.loc[i]
            object2 = df.loc[j]

            distance = mixed_dissimilarity(object1, object2, attribute_types)
            dissimilarity_matrix.iloc[i, j] = distance
            dissimilarity_matrix.iloc[j, i] = distance
    
    return dissimilarity_matrix


""" Write a function named mixed_dissimilarity to find the dissimilarity between
any pair of objects, following the method for mixed attribute types at the bottom of
Section 06-2 of the notes.
 The function should accept three arguments: two objects which have some number
of attributes (e.g., two rows of a pandas DataFrame), and a list or array of strings
indicating the type of each attribute in the dataset, in order.
 The attribute types should be used to determine how to incorporate the distance for
each attribute. The function should distinguish between symmetric binary and
asymmetric binary attributes and treat them accordingly.
 The function is not required to account for missing values (assume there will be no
missing values).
 The function should assume that all variables that can be normalized have already
been normalized. """