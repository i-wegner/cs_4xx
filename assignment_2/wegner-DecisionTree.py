import pandas as pd
from sklearn.model_selection import train_test_split
from sklearn import tree

rand_state = 200514620
df = pd.read_csv('wegner-risk-data.csv', header = 0)
train, test = train_test_split(df, train_size = 0.8, random_state = rand_state)

dtree1 = tree.DecisionTreeClassifier(criterion = 'entropy', random_state = rand_state)

tree_text = tree.export_text(dtree1, feature_names=['Elevation', 'Precipitation', 'Risk Level'])
with open('wegner-first-tree.txt', 'w') as f:
    print(tree_text, file = f)