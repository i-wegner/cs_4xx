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

mat = dissimilarityMatrix(df)

total = [0] * len(df)
for i in range(len(df)):
    total[i] = sum(mat[i])

min_ = min(total)
minimum = 100000
idx = total.index(min(total))
for i, object in enumerate(total):
    if object < minimum:
        min_index = i
        minimum = object

print(min_index, minimum)
print(idx, min_)


"""
tree_text = tree.export_text(dtree1, feature_names = ['Elevation', 'Precipitation'])
with open('wegner-first-tree.txt', 'w') as f:
    print(tree_text, file = f)
    print(f'Total number of nodes: {dtree1.tree_.node_count}', file = f)
    print(f'Maximum depth: {dtree1.tree_.max_depth}', file = f)
    print(f'Minimum node size: {min(dtree1.tree_.n_node_samples)}', file = f)
    impurity = 0
    for i in range(dtree1.tree_.node_count):
        if dtree1.tree_.feature[i] == -2:
            impurity += dtree1.tree_.impurity[i]
    ave_leaf_impurity = impurity / dtree1.get_n_leaves()
    print(f'Average impurity of leaves: {ave_leaf_impurity}', file = f)
        # Consider that the tree is unrestricted (it is split until the training data is perfectly classified),
        # thus we end up with 0.0
    print(f'Accuracy score: {dtree1.score(X_test, y_test)}', file = f)

y_pred = dtree1.predict(X_test)
risk_matrix = ConfusionMatrixDisplay.from_predictions(y_test, y_pred)

risk_matrix.figure_.savefig('wegner-confusion-matrix.png')
plt.show()
"""