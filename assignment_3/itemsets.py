import pandas as pd
from itertools import chain, combinations
import numpy as np
table1 = {
    'TID' : ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10'],
    'A' : [1, 0, 1, 0, 0, 0, 0, 4, 0, 0],
    'B' : [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    'C' : [1, 6, 2, 4, 3, 1, 8, 0, 1, 0],
    'D' : [14, 0, 4, 0, 1, 13, 0, 7, 10, 18]
}
table1 = pd.DataFrame(table1)

def powerset(set):
    s = list(set)
    l = []
    power_set = list(chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1)))

    for i in range(len(power_set)):
        l.insert(i, list(power_set[i]))

    return l


""" supp_ad = 0
for i in range(len(table1)):
    if (table1['A'][i] != 0 and table1['D'][i] != 0):
        print(table1['A'][i], table1['D'][i])
        supp_ad += 1
supp_ad = supp_ad / len(table1)

print(supp_ad)

def support(table):

    pass
 """

l = powerset('ABCD')

table2Test = {
    'Itemset' : l,
    'Support' : np.zeros(len(l))
}
table2Test = pd.DataFrame(table2Test)

def support(table):
    for i, itemset in enumerate(table['Itemset']):
        items = itemset.split(', ')


table2 = {
    'Itemset' : ['A', 'B', 'C', 'D', 'A,B', 'A,C', 'A,D', 'B,C', 'B,D', 'C,D', 'A,B,C', 'A,B,D', 'A,C,D', 'B,C,D', 'A,B,C,D'],
    'Support' : [0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00, 0.00]
}
for i, itemset in enumerate(table2['Itemset']):
    items = itemset.split(',')

    supp = (table1[items] != 0).all(axis = 1).mean()
    table2['Support'][i] = supp
table2 = pd.DataFrame(table2)
print(type(table2Test['Itemset'][0]))
print(type(table2['Itemset'][0]))
print(table2Test)