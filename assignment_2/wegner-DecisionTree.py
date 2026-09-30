import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree

rand_state = 200514620
df = pd.read_csv('wegner-risk-data.csv', header = 0)
train, test = train_test_split(df, train_size = 0.8, random_state = rand_state)

dtree1 = tree.DecisionTreeClassifier(criterion = 'entropy', random_state = rand_state)

dtree1.fit(train[['Elevation', 'Precipitation']], train['Risk Level'])

print(f'{sum(dtree1.tree_.impurity) / dtree1.tree_.node_count}') # average impurity of the entire tree, not just the leaf nodes

tree_text = tree.export_text(dtree1, feature_names = ['Elevation', 'Precipitation'])
with open('wegner-first-tree.txt', 'w') as f:
    print(tree_text, file = f)
    print(f'Total number of nodes: {dtree1.tree_.node_count}', file = f)
    print(f'Maximum depth: {dtree1.tree_.max_depth}', file = f)
    print(f'Minimum node size: {min(dtree1.tree_.n_node_samples)}', file = f)
    print(f'A{sum(dtree1.tree_.impurity) / dtree1.tree_.node_count}')


print(dtree1.tree_.n_leaves)
print(dtree1.tree_.feature) # returns an array with the values 0, 1, -2 where -2 represents a leaf node

# traverse the tree and identify the leaf nodes
for i in range(dtree1.tree_.node_count):
    if dtree1.tree_.feature[i] == -2:
        print('leaf!')