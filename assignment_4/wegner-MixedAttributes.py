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
        return series * 0 # if all the values are the same, then the normalized values = 0

    else:
        series = (series - s_min) / (s_max - s_min) # formula to normalize values from 06-2

    return series
# update the dataframe with normalized/rank transformed values for the linear attributes
df['MedianWage'] = normalize_variable(df['MedianWage'])
df['Ranking'] = normalize_variable(df['Ranking'])
df['NumberOfEmployees'] = rank_transform(df['NumberOfEmployees'])

# list of attribute types, in order based on given dataset
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
            distance.append(np.abs(object1.iloc[i] - object2.iloc[i])) # distance between linear, nonlinear, and ordinal attributes
            delta.append(1) # delta always = 1 for linear, nonlinear, and ordinal attributes

        elif item == 'nominal':
            if object1.iloc[i] != object2.iloc[i]:
                distance.append(1) # distance between two nominal objects = 1 everytime they are different
            else:
                distance.append(0) # distance between two nominal objects = 0 everytime they are the same
            delta.append(1) # delta always = 1 for nominal attributes

        elif item == 'symmetric binary':
            if object1.iloc[i] != object2.iloc[i]:
                distance.append(1)
            else: # distance = 1 for sym. binary if they are different, = 0 otherwise
                distance.append(0)
            delta.append(1) # delta always = 1 for sym. binary attributes

        elif item == 'asymmetric binary':
            if object1.iloc[i] == 0 and object2.iloc[i] == 0:
                distance.append(0)
                delta.append(0)
            else: # asymmetric binary attributes are only counted if at least one is non-zero
                distance.append(1)
                delta.append(1)

        numerator += delta[i] * distance[i]

    denominator = sum(delta)
    object_distance = numerator / denominator # all good unless we are only compary asym. binary attributes of all zeros

    return object_distance

def dissimilarityMatrix(df):
    n = len(df) # save overhead compute for each nested loop calculation
    dissimilarity_matrix = pd.DataFrame(np.zeros((n, n))) # n*n matrix of all zeros as pd DataFrame

    # compare all pairs of objects 
    for i in range(n):
        for j in range(i + 1, n):
            object1 = df.loc[i]
            object2 = df.loc[j]

            distance = mixed_dissimilarity(object1, object2, attribute_types)
            # since matrix is symmetrical, we update both applicable cells
            dissimilarity_matrix.iloc[i, j] = distance
            dissimilarity_matrix.iloc[j, i] = distance
    
    return dissimilarity_matrix

dissimilarity_matrix = dissimilarityMatrix(df)

def medoid_cost(dissimilarity_matrix, df):
    n = len(df)
    cost_list = [0] * n # list of n zeros to to update with the associated costs

    for i in range(n):
        cost_list[i] = sum(dissimilarity_matrix[i]) # sum the values of each row and update the corresponding index in the list

    min_index = cost_list.index(min(cost_list)) # index of smallest average dissimilarity medoid
    total_medoid_cost = cost_list[min_index] # cost associated with the smallest average dissimilarity medoid
    ave_medoid_cost = total_medoid_cost / (len(cost_list) - 1) # average dissimilarity among attributes on the medoid with the smallest average dissimilarity
    
    return min_index, total_medoid_cost, ave_medoid_cost

min_index, total_medoid_cost, ave_medoid_cost = medoid_cost(dissimilarity_matrix, df)

# write out to .txt file
with open('wegner-medoid.txt', 'w') as file:
    file.write(f'Medoid index: {min_index}\n')
    file.write(f'Total medoid cost: {total_medoid_cost}\n')
    file.write(f'Average medoid cost: {ave_medoid_cost}')