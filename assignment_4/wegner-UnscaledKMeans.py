import pandas as pd
import numpy as np

df = pd.read_csv('different_scales.csv')
df2 = df.copy()

def normalize_variable(df): # normalize linear attributes(s)
    attributes = df.columns.tolist()
    for attribute in attributes:
        s_min = df[attribute].min()
        s_max = df[attribute].max()

        if s_min == s_max:
            return df[attribute] * 0

        else:
            df[attribute] = (df[attribute] - s_min) / (s_max - s_min)

normalize_variable(df2)

def standardize_varibale():
    pass