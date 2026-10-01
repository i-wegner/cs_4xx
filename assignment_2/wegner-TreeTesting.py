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

trees = [dtree1, dtree7] # list for enumerate(). Was reduced from all to two trees after observing performance

print('Mean cross validation scores:')
for i, t in enumerate(trees, start = 1):
    print(f'Tree {i}: {cross_val_score(t, X_train, y_train).mean()}')

dtree1.fit(X_train, y_train) # non-limited tree
dtree7.fit(X_train, y_train) # best performing tree

with open('wegner-tree-compare.txt', 'w') as f:
    for i, t in enumerate(trees, start = 1):
        print(f'=========== Tree {i} ===========\n', file = f)
        print(tree.export_text(t), file = f)
        #print(tree_text1, file = f)
        print(f'Total number of nodes: {t.tree_.node_count}', file = f)
        print(f'Maximum depth: {t.tree_.max_depth}', file = f)
        print(f'Minimum node size: {min(t.tree_.n_node_samples)}', file = f)

        impurity = 0
        for j in range(t.tree_.node_count):
            if t.tree_.feature[j] == -2: # -2 marks a leaf
                impurity += t.tree_.impurity[j]
        ave_leaf_impurity = impurity / t.get_n_leaves()
        print(f'Average impurity of leaves: {ave_leaf_impurity}', file = f)

        print(f'Accuracy score: {t.score(X_test, y_test)}', file = f)
        print('\n', file = f)