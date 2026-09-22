import numpy as np
from numpy import random as rand

num_rows = 200
rng = rand.default_rng(200514620)

elevation = rng.uniform(0, 500, num_rows)
precipitation = rng.normal(100, 80, num_rows)

