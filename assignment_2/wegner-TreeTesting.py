from sklearn import tree
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score

rand_state = 200514620

X, y = make_classification(n_samples = 500, n_features = 10, n_informative = 3, n_redundant = 0, n_classes = 5, n_clusters_per_class = 1, random_state = rand_state)

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2, random_state = rand_state)

dtree1 = tree.DecisionTreeClassifier(criterion = 'entropy', random_state = rand_state)
dtree1.fit(X_train, y_train)
dtree2 = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth = 5, random_state = rand_state)
dtree2.fit(X_train, y_train)
dtree3 = tree.DecisionTreeClassifier(criterion = 'entropy', min_samples_split = 13, random_state = rand_state)
dtree3.fit(X_train, y_train)
dtree4 = tree.DecisionTreeClassifier(criterion = 'entropy', min_samples_split = 0.05, random_state = rand_state)
dtree4.fit(X_train, y_train)
dtree5 = tree.DecisionTreeClassifier(criterion = 'entropy', min_impurity_decrease = 0.05, random_state = rand_state)
dtree5.fit(X_train, y_train)
dtree6 = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth = 5, min_samples_leaf = 13, random_state = rand_state)
dtree6.fit(X_train, y_train)

trees = [dtree1, dtree2, dtree3, dtree4, dtree5, dtree6]

print('Total number of nodes:')
for i, t in enumerate(trees, start=1):
    print(f'Tree {i}: {t.tree_.node_count}')

print('The maximum depth:')
for i, t in enumerate(trees, start = 1):
    print(f'Tree {i}: {t.tree_.max_depth}')

print('The minimum node size:')
for i, t in enumerate(trees, start = 1):
    print(f'Tree {i}: {min(t.tree_.n_node_samples)}')

print('The accuracy score:')
for i, t in enumerate(trees, start = 1):
    print(f'Tree {i}: {t.score(X_test, y_test)}')

