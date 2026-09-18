import pandas as pd
import numpy as np
from numpy import random as rand

rng = rand.default_rng(seed = 69)
num_rows = 1000
name_dist = rng.choice(['Noah', 'Helene', 'Clara', 'Emilia', 'Matteo', 'Elias', 'Hana'], num_rows, p = [0.17, 0.19, 0.13, 0.14, 0.11, 0.07, 0.19])
part_dist = rng.choice(['P1', 'P2', 'P3', 'P4', 'P5', 'P6', 'P7', 'P8', 'P9'], num_rows, p = [0.17, 0.03, 0.12, 0.11, 0.08, 0.14, 0.09, 0.07, 0.19])
city_dist = rng.choice(['Berlin', 'Hamburg', 'Munich', 'Cologne', 'Leipzig', 'Nuremberg'], num_rows, p = [0.27, 0.08, 0.21, 0.15, 0.11, 0.18])

synth_data = pd.DataFrame({'Customer' : name_dist,
                   'PartNum' : part_dist,
                   'City' : city_dist})
synth_data.to_csv('sales-wegner.csv', index = False, header = True)