from sklearn import tree
from sklearn.datasets import make_classification
from sklearn.model_selection import train_test_split
from sklearn.model_selection import cross_val_score
rand_state = 200514620

X, y = make_classification(n_samples = 500, n_features = 10, n_informative = 3, n_redundant = 0, n_classes = 5, n_clusters_per_class = 1, random_state = rand_state)
X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = .2, random_state = rand_state)

dtree1 = tree.DecisionTreeClassifier(criterion = 'entropy', random_state = rand_state)
dtree2 = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth = 5, random_state = rand_state)
dtree3 = tree.DecisionTreeClassifier(criterion = 'entropy', min_samples_split = 13, random_state = rand_state)
dtree4 = tree.DecisionTreeClassifier(criterion = 'entropy', min_samples_split = 0.05, random_state = rand_state)
dtree5 = tree.DecisionTreeClassifier(criterion = 'entropy', min_impurity_decrease = 0.05, random_state = rand_state)
dtree6 = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth = 5, min_samples_leaf = 13, random_state = rand_state)
dtree7 = tree.DecisionTreeClassifier(criterion = 'entropy', max_depth = 5, min_samples_split = 0.05, random_state = rand_state)

dtree1.fit(X_train, y_train)
dtree7.fit(X_train, y_train)

tree_text1 = tree.export_text(dtree1)
with open('wegner-tree-compare.txt', 'w') as f:
    print(tree_text1, file = f)
    print(f'Total number of nodes: {dtree1.tree_.node_count}', file = f)
    print(f'Maximum depth: {dtree1.tree_.max_depth}', file = f)
    print(f'Minimum node size: {min(dtree1.tree_.n_node_samples)}', file = f)
    impurity = 0
    for i in range(dtree1.tree_.node_count):
        if dtree1.tree_.feature[i] == -2:
            impurity += dtree1.tree_.impurity[i]
    ave_leaf_impurity = impurity / dtree1.get_n_leaves()
    print(f'Average impurity of leaves: {ave_leaf_impurity}', file = f)
    print(f'Accuracy score: {dtree1.score(X_test, y_test)}', file = f)

tree_text7 = tree.export_text(dtree7)
with open('wegner-tree-compare.txt', 'a') as f:
    print(tree_text7, file = f)
    print(f'Total number of nodes: {dtree7.tree_.node_count}', file = f)
    print(f'Maximum depth: {dtree7.tree_.max_depth}', file = f)
    print(f'Minimum node size: {min(dtree7.tree_.n_node_samples)}', file = f)
    impurity = 0
    for i in range(dtree7.tree_.node_count):
        if dtree7.tree_.feature[i] == -2:
            impurity += dtree7.tree_.impurity[i]
    ave_leaf_impurity = impurity / dtree7.get_n_leaves()
    print(f'Average impurity of leaves: {ave_leaf_impurity}', file = f)
    print(f'Accuracy score: {dtree7.score(X_test, y_test)}', file = f)