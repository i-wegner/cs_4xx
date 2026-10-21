import pandas as pd
from itertools import chain, combinations # packages required for most efficient powerset function

table1 = {
    'TID' : ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10'],
    'A' : [1, 0, 1, 0, 0, 0, 0, 4, 0, 0],
    'B' : [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    'C' : [1, 6, 2, 4, 3, 1, 8, 0, 1, 0],
    'D' : [14, 0, 4, 0, 1, 13, 0, 7, 10, 18]
}
table1 = pd.DataFrame(table1) # convert dictionary into dataframe for pandas capabilities

# powerset function referenced from substack (see README.md) with some revisions to return a list of lists
def powerset(set):
    s = list(set)
    l = []
    power_set = list(chain.from_iterable(combinations(s, r) for r in range(1, len(s) + 1)))

    for i in range(len(power_set)):
        l.insert(i, list(power_set[i]))

    return l

# support function to compute support value for every itemset and update in table 'support' column
def support(table1, table2):
    support_list = []

    for itemset in table2['Itemset']:
        supp = (table1[itemset] != 0).all(axis = 1).mean()
        support_list.append(supp)

    table2['Support'] = support_list

l = powerset('ABCD')

table2 = {
    'Itemset' : l,
    'Support' : np.zeros(len(l))
}
table2 = pd.DataFrame(table2) # convert dictionary into dataframe for pandas capabilities
support(table1, table2)

freq_itemsets = table2[table2['Support'] >= 0.2]