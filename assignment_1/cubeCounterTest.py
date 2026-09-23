import time
import numpy as np
import pandas as pd
start_time = time.time()

df = pd.read_csv('sales-wegner.csv', header = 0)
i_cust = df['Customer'].drop_duplicates() # layer
j_part = df['PartNum'].drop_duplicates() # row
j_part = j_part.sort_values() # sort the series alphabetically/numerically
k_city = df['City'].drop_duplicates() # column

# build dictionaries for each attribute
I = 0
cust_dict = {}
for row in i_cust:
    cust_dict.update({I : row})
    I += 1

J = 0
part_dict = {}
for row in j_part:
    part_dict.update({J : row})
    J += 1

K = 0
city_dict = {}
for row in k_city:
    city_dict.update({K : row})
    K += 1

# instatiate 3d numpy array
cube = np.zeros((I + 1, J + 1, K + 1), dtype = int)


for x in range(df.shape[0]):
    cust = df.iloc[x, 0]
    part = df.iloc[x, 1]
    city = df.iloc[x, 2]

    temp_layer = next(key for key, value in cust_dict.items() if value == cust)
    temp_row = next(key for key, value in part_dict.items() if value == part)
    temp_column = next(key for key, value in city_dict.items() if value == city)

    cube[temp_layer, temp_row, temp_column] += 1

# sum marginal totals
for i in range(I):
    for j in range(J):
        cube[i, j, K] = np.sum(cube[i, j, :])
    for k in range(K):
        cube[i, J, k] = np.sum(cube[i, :, k])

# sum last layer (total layer) totals
for j in range(J + 1):
    for k in range(K + 1):
        cube[I, j, k] = np.sum(cube[:, j, k])
    cube[I, J, K] = np.sum(cube[I, J, :])

# Print all marginal totals by customer
for i in range(I):
    print(f"{cust_dict.get(i)}'s purchases by part:")
    for row in range(J):
        print(f"Part {part_dict.get(row)}: {cube[i, row, K]}")
    print(f"\n{cust_dict.get(i)}'s purchases by city:")
    for column in range(K):
        print(f"{city_dict.get(column)}: {cube[i, J, column]}")
    print('\n-------------\n')

# print non-zero marginal totals in Ordered Set Representation
# every non-zero value from the marginal total column/row for each customer
# as well as every non-zero total from the absolute total layer, only excluding the absolute total itself
# not printing out cube[I, J, K] because it is the absolute total, and not a marginal total
""" for i in range(I):
    for j in range(J):
        if cube[i, j, K] != 0:
            print(f"{cust_dict.get(i)}, {part_dict.get(j)}, ANY | {cube[i, j, K]}")
    for k in range(K):
        if cube[i, J, k] != 0:
            print(f"{cust_dict.get(i)}, ANY, {city_dict.get(k)} | {cube[i, J, k]}")
    print('\n-------------\n')

    if I - i == 1:
        for j in range(J):
            for k in range(K):
                if cube[I, j, k] != 0:
                    print(f"ANY, {part_dict.get(j)}, {city_dict.get(k)} | {cube[I, j, k]}")
        print('\n-------------\n')
        for j in range(J):
            if cube[I, j, K] != 0:
                print(f"ANY, {part_dict.get(j)}, ANY | {cube[I, j, K]}")
        for k in range(K):
            if cube[I, J, k] != 0:
                print(f"ANY, ANY, {city_dict.get(k)} | {cube[I, J, k]}") """

print("--- %s seconds ---" % (time.time() - start_time))