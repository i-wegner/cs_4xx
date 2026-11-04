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

dissimilarity_matrix = dissimilarityMatrix(df)

def medoid_cost(dissimilarity_matrix, df):
    cost_list = [0] * len(df)

    for i in range(len(df)):
        cost_list[i] = sum(dissimilarity_matrix[i])

    min_index = cost_list.index(min(cost_list))
    total_medoid_cost = cost_list[min_index]
    ave_medoid_cost = total_medoid_cost / (len(cost_list) - 1)
    
    return min_index, total_medoid_cost, ave_medoid_cost

total_medoid_cost, min_index, ave_medoid_cost = medoid_cost(dissimilarity_matrix, df)

with open('wegner-medoid.txt', 'w') as file:
    file.write(f'Medoid index: {min_index}\n')
    file.write(f'Total medoid cost: {total_medoid_cost}\n')
    file.write(f'Average medoid cost: {ave_medoid_cost}')