import pandas as pd
from itertools import chain, combinations # packages required for most efficient powerset function
import numpy as np
import math

# =============== Q3, Parts 1, 2, 3 ===============

table1 = {
    'TID' : ['T1', 'T2', 'T3', 'T4', 'T5', 'T6', 'T7', 'T8', 'T9', 'T10'],
    'A' : [1, 0, 1, 0, 0, 0, 0, 4, 0, 0],
    'B' : [0, 0, 0, 0, 0, 0, 0, 0, 1, 0],
    'C' : [1, 6, 2, 4, 3, 1, 8, 0, 1, 0],
    'D' : [14, 0, 4, 0, 1, 13, 0, 7, 10, 18],
    'E' : [14, 0, 4, 0, 1, 13, 0, 7, 10, 18]
}
table1 = pd.DataFrame(table1) # convert dictionary into dataframe for pandas capabilities

# powerset function referenced from substack (see README.md) with some revisions to return a list of lists
def powerSet(set):
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


power_string = "".join(table1.columns[1:])
l = powerSet(power_string)

table2 = {
    'Itemset' : l,
    'Support' : np.zeros(len(l))
}
table2 = pd.DataFrame(table2) # convert dictionary into dataframe for pandas capabilities
support(table1, table2)
#print(f'=== Itemset Table with Support Values ===\n {table2}\n')

freq_itemsets = table2[table2['Support'] >= 0.2]
#print(f'=== Itemset Table of Frequent Itemsets (minconf = 0.2) ===\n {freq_itemsets}\n')

# ============ Q3, Parts 5, 6, 7, 8, 9 ============

table3 = {
    'TID' : ['T1', 'T2', 'T3', 'T4', 'T5'],
    'A' : [1, 1, 1, 1, 1],
    'B' : [1, 1, 0, 0, 1],
    'C' : [1, 1, 1, 1, 1],
    'D' : [0, 1, 1, 1, 1],
    'E' : [0, 1, 0, 1, 0],
    'F' : [1, 0, 0, 0, 0]
}
table3 = pd.DataFrame(table3)

def apriori (table1):
    power_string = "".join(table1.columns[1:])
    l = list(power_string)
    stop_slice = math.comb(len(l), 1) + math.comb(len(l), 2) + math.comb(len(l), 3) + math.comb(len(l), 4)
    start_slice = math.comb(len(l), 1) + math.comb(len(l), 2)
    candidate_1 = powerSet(l)[start_slice + 1:stop_slice]
    print(candidate_1)

    # Possible method for candidate itemsets


apriori(table3)
#print(type(table3['A']))