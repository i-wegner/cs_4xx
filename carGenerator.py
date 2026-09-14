# A1Q3 (b)
# Generate synthetic car data

import numpy as np
from numpy import random as rand
import pandas as pd

rng = rand.default_rng(seed = 69)
colour_dist = rng.choice(['White', 'Black', 'Gray', 'Silver', 'Blue', 'Red', 'Green', 'Brown', 'Orange', 'Gold', 'Purple'], 100000, p = [.246, .217, .198, .141, .089, .075, .02, .009, .0031, .001, .0009])
model_dist = rng.choice(['Ford F-Series', 'Toyota RAV4', 'GMC Seirra', 'Honda CRV', 'Chevrolet Silverado', 'RAM 1500', 'Hyundai Tucson', 'Nissan Rogue', 'Ford Escape', 'Subaru Crosstrek'], 100000, p = [0.261, 0.131, 0.101, 0.096, 0.093, 0.073, 0.071, 0.061, 0.057, 0.056])

synthetic_car = pd.DataFrame({'Colour' : colour_dist,
                             'Model' : model_dist})
synthetic_car.to_csv("cars-wegner.csv", index = False, header = False)