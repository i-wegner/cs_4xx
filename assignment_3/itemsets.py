import pandas as pd

table1 = {
    'TID' : ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10'],
    'A' : [1, 0, 1, 0, 0, 0, 0, 4, 0, 0],
    'B' : [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    'C' : [1, 6, 2, 4, 3, 1, 8, 0, 1, 0],
    'D' : [14, 0, 4, 0, 1, 13, 0, 7, 10, 18]
}
table1 = pd.DataFrame(table1)

table2 = {
    'Itemset' : ['A', 'B', 'C', 'D', 'A,B', 'A,C', 'A,D', 'B,C', 'B,D', 'C,D', 'A,B,C', 'A,B,D', 'A,C,D', 'B,C,D', 'A,B,C,D'],
    'Support' : [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
}

for i, itemset in enumerate(table2['Itemset']):
    items = itemset.split(',')
    print((table1[items] != 0).sum())

    #support = sum(table1[items] != 0)


#table2 = pd.DataFrame(table2)