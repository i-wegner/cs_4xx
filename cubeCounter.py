#A1Q4 (a)

import numpy as np
import pandas as pd

df = pd.read_csv('cps.csv', header = 0)
i_cust = df['Customer'].drop_duplicates() # layer
j_part = df['PartNum'].drop_duplicates() # row
j_part = j_part.sort_values() # sort the series alphabetically/numerically
k_city = df['City'].drop_duplicates() # column

num_cust = 0
cust_dict = {}

num_part = 0
part_dict = {}

num_city = 0
city_dict = {}

for row in i_cust:
    cust_dict.update({num_cust : row})
    num_cust += 1

for row in j_part:
    part_dict.update({num_part : row})
    num_part += 1

for row in k_city:
    city_dict.update({num_city : row})
    num_city += 1

I = num_cust + 1
J = num_part + 1
K = num_city + 1

cube = np.zeros((I, J, K), dtype = int)

for x in range(df.shape[0]):
    cust = df.iloc[x, 0]
    part = df.iloc[x, 1]
    city = df.iloc[x, 2]

    temp_layer = next(key for key, value in cust_dict.items() if value == cust)
    temp_row = next(key for key, value in part_dict.items() if value == part)
    temp_column = next(key for key, value in city_dict.items() if value == city)

    cube[temp_layer, temp_row, temp_column] += 1

for i in range(I):
    for j in range(J):
        cube[i, j, num_city] = np.sum(cube[i, j, :])
    for k in range(K):
        cube[i, num_part, k] = np.sum(cube[i, :, k])


for j in range(J):
    for k in range(K):
        cube[num_cust, j, k] = np.sum(cube[:, j, k])
