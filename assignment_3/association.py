import pandas as pd
import numpy as np
from itertools import chain, combinations

# support function to compute support value for every itemset and update in table 'support' column
# modify table2 in place with updated support values. no return value
def support(table1, table2):
    support_list = []

    for itemset in table2['Itemset']:
        supp = (table1[itemset] != 0).all(axis = 1).mean()
        support_list.append(supp)

    table2['Support'] = support_list

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

def apriori (table1, min_support = 0.4):
    items = [[item] for item in table1.columns[1:]]
    C_1 = pd.DataFrame({
        'Itemset' : items,
        'Support' : np.zeros(len(items))
    })

    support(table1, C_1)

    L_1 = C_1[C_1['Support'] >= min_support]
    # ** Modification from itemsets.py **
    frequent_itemsets = [L_1.copy()] # need a list of frequent itemsets for association rules
    L_prev = L_1
    k = 2

    while not L_prev.empty:
        C_k = candidateTable(L_prev, k)
        support(table1, C_k)
        L_prev = C_k[C_k['Support'] >= min_support]

        if L_prev.empty:
            break
        frequent_itemsets.append(L_prev.copy())
        k += 1
    return pd.concat(frequent_itemsets, ignore_index = True)

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

def associatoneRules(table1, frequent_itemsets, min_conf = 0.6):
    rules = []

    for i, row in frequent_itemsets.iterrows():
        itemset = row['Itemset']

        if len(itemset) < 2:
            continue

        itemset_support = row['Support']

        for r in range(1, len(itemset)):
            for antecedent in combinations(itemset, r):
                antecedent = list(antecedent)

                consequent = [
                    item for item in itemset
                    if item not in antecedent
                ]

                supp = (table1[antecedent] != 0).all(axis = 1).mean()
                confidence = itemset_support / supp

                if confidence >= min_conf:
                    rules.append({
                        'Antecedent' : antecedent,
                        'Consequent' : consequent,
                        'Support' : itemset_support,
                        'Confidence' : confidence
                    })
    return pd.DataFrame(rules)

frequent_itemsets = apriori(table3)
table4 = associatoneRules(table3, frequent_itemsets)
print(table4)