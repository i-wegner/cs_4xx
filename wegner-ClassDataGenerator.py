import numpy as np
from numpy import random as rand

num_rows = 20
rng = rand.default_rng(200514620)

elevation = rng.uniform(0, 500, num_rows)
precipitation = rng.normal(100, 80, num_rows)
precipitation[precipitation < 0] = 0 # boolean mask directly updates the array in place

def riskLevel(elevation, precipitation):
    # create a condition list of boolean numpy arrays
    # each condition creates a numpy array of size num_rows (the size of the arrays containing the data, they must be equal in size to evaluate the condition)
    cond_list = [
        (elevation < 125) & (precipitation < 70),                                         # low condition 1
        (elevation >= 125) & (elevation < 250) & (precipitation < 95),                    # low condition 2
        (elevation >= 250) & (elevation < 500) & (precipitation < 140),                   # low condition 3

        (elevation < 125) & (precipitation >= 70) & (precipitation < 140),                # medium condition 1
        (elevation >= 125) & (elevation < 250) & (precipitation <= max(precipitation)),    # medium condition 2
        (elevation >= 250) & (elevation < 500) & (precipitation <= max(precipitation)),    # medium condition 3

        (elevation < 125) & (precipitation <= max(precipitation))                          # high condition 1
    ]

    # 
    choice_list = [
        'low', 'low', 'low',

        'medium', 'medium', 'medium',

        'high'
    ]
 
    # instatiate an array drawn from the elements in choice_list, depending on the conditions in cond_list
    # the output at position m is the m-th element of the array in choice_list where the m-th element of the corresponding array in cond_list is True.
    risk_level = np.select(cond_list, choice_list, default = '')

    return risk_level

risk_level = riskLevel(elevation, precipitation)
print(risk_level)