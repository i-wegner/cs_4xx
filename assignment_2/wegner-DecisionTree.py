import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree
from sklearn.metrics import ConfusionMatrixDisplay
import matplotlib.pyplot as plt

rand_state = 200514620
df = pd.read_csv('wegner-risk-data.csv', header = 0)
X = df.iloc[:, :-1]
y = df.iloc[:, -1]

X_train, X_test, y_train, y_test = train_test_split(X, y, test_size = 0.8, random_state = rand_state)

dtree1 = tree.DecisionTreeClassifier(criterion = 'entropy', random_state = rand_state)
dtree1.fit(X_train[['Elevation', 'Precipitation']], y_train)

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
    ave_leaf_impurity = impurity / dtree1.tree_.n_leaves
    print(f'Average impurity of leaves: {ave_leaf_impurity}', file = f)
    print(f'Accuracy score: {dtree1.score(X_test, y_test)}', file = f)

y_pred = dtree1.predict(X_test)
risk_matrix = ConfusionMatrixDisplay.from_predictions(y_test, y_pred)

risk_matrix.figure_.savefig('wegner-confusion-matrix.png')
plt.show()