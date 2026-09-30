from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.datasets import make_classification

rand_state = 200514620

X, y = make_classification(n_samples = 500, n_features = 10, n_informative = 3, n_redundant = 0, n_classes = 5, n_clusters_per_class = 1, random_state = rand_state)

X_train, x_test, y_train, y_test = train_test_split(X, y, test_size = .2)

dtree1 = tree.DecisionTreeClassifier(criterion = 'entropy', random_state = rand_state)