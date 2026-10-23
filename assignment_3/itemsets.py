import pandas as pd
from itertools import chain, combinations # packages required for most efficient powerset function
import numpy as np
import math

# =============== Q3, Parts 1, 2, 3 ===============

# Table 1 from 05-1 handout
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
# modify table2 in place with updated support values. no return value
def support(table1, table2):
    support_list = []

    for itemset in table2['Itemset']:
        supp = (table1[itemset] != 0).all(axis = 1).mean()
        support_list.append(supp)

    table2['Support'] = support_list

# powersetTable function is only useful for generating Table 2 from 05-1 handout. 
def powersetTable(table1):
    power_string = "".join(table1.columns[1:])
    items = powerSet(power_string)

    table2 = {
        'Itemset' : items,
        'Support' : np.zeros(len(items))
    }
    table2 = pd.DataFrame(table2) # convert dictionary into dataframe for pandas capabilities
    return table2

def candidateTable(L_prev, k):
    candidate_itemsets = []
    if k == 2:
        for i in range(len(L_prev)):
            for j in range(i + 1, len(L_prev)):
                candidate_itemsets.append(L_prev['Itemset'].iloc[i] + L_prev['Itemset'].iloc[j])
    else:
        for i in range(len(L_prev)):
            for j in range(i + 1, len(L_prev)):
                if L_prev['Itemset'].iloc[i][:-1] == L_prev['Itemset'].iloc[j][:-1]:
                    list1 = L_prev['Itemset'].iloc[i]
                    list2 = list(L_prev['Itemset'].iloc[j][-1])
                    candidate_itemsets.append(list1 + list2)
                    # N.T.I -> full pruning check
                        # Starting from the last element, iterate through down to the first element and prune each ieteration

    C_k = pd.DataFrame({
        'Itemset' : candidate_itemsets,
        'Support' : np.zeros(len(candidate_itemsets))
    })

    return C_k

table2 = powersetTable(table1)
support(table1, table2)
#print(f'=== Itemset Table with Support Values ===\n {table2}\n')

freq_itemsets = table2[table2['Support'] >= 0.2]
#print(f'=== Itemset Table of Frequent Itemsets (minconf = 0.2) ===\n {freq_itemsets}\n')


# ============ Q3, Parts 5, 6, 7, 8, 9 ============

# Table 3 from 05-1 handout
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

def apriori (table1, min_support = 0.4):
# pass 1
    #1.
    items = [[item] for item in table1.columns[1:]]
    C_1 = pd.DataFrame({
        'Itemset' : items,
        'Support' : np.zeros(len(items))
    })

    
    #2.
    support(table1, C_1)

    #3.
    L_1 = C_1[C_1['Support'] >= min_support]

    # display C_1 and L_1 for the purpose of following the algorithm as it iterates
    print(f'============ Candidate Itemset (C_1) ============\n {C_1}\n')
    print(f'==== Frequent Itemset (L_1, support >= {min_support}) ====\n {L_1}\n')

# pass [2, k]
    L_prev = L_1
    k = 2

    while not L_prev.empty:
        C_k = candidateTable(L_prev, k)
        support(table1, C_k)
        L_prev = C_k[C_k['Support'] >= min_support]

        if L_prev.empty:
            print(f'***There are no further frequent itemsets to consider. Process complete after {k} iterations.***')
            break
        else:
            print(f'\n{"=" * 15} Pass #{k} {"=" * 15}')
            print(f'\nCandidate Itemsets (C_{k}):')
            print(C_k.to_string(index=False))

            print(f'\nFrequent Itemsets (L_{k}):')
            print(L_prev.to_string(index=False))
            print()

            k += 1

apriori(table3)