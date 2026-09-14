#A1Q4 (a)

import numpy as np
import pandas as pd

df = pd.read_csv('cps.csv', header = 0)
i_cust = df['Customer'].drop_duplicates() # layer
j_part = df['PartNum'].drop_duplicates() # row
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

cube = np.zeros((num_cust + 1, num_part + 1, num_city + 1), dtype = int)

print(cube)