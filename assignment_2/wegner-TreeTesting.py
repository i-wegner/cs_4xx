from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.datasets import make_classification

rand_state = 200514620

X, y = make_classification(n_samples = 500, n_features = 10, n_informative = 3, n_redundant = 0, n_classes = 5, n_clusters_per_class = 1, random_state = rand_state)

X_train, x_test, y_train, y_test = train_test_split(X, y, test_size = .2)

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

print(dtree1.tree_.max_depth)

# This code produces a max depth of both 10 & 11 for dtree1, why?
# Q: Fitting the tree on specific attributes vs on the entire training set
# Q: Fitting the tree before any information can be printed
# Q: Tree has to be fit in order to 'check' any tree details (dtree1.tree_.max_depth). Why?