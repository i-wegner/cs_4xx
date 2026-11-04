import pandas as pd
import numpy as np

df = pd.read_csv('different_scales.csv')
# copies of df so that df is unchanged when we normalize/standardize
df2 = df.copy()
df3 = df.copy()

def normalize_variable(df): # normalize linear attributes(s)
    attributes = df.columns.tolist() # instatiate list of column names from df
    for attribute in attributes:
        s_min = df[attribute].min()
        s_max = df[attribute].max()

        if s_min == s_max:
            return df[attribute] * 0

        else:
            df[attribute] = (df[attribute] - s_min) / (s_max - s_min)

normalize_variable(df2)

def standardize_variable(df):
    n = len(df)
    attributes = df.columns.tolist()
    ave = df.mean()
    std = df.std() # pandas std() default ddof = 1 for sample std
    

    for attribute in attributes:
        df[attribute] = (df[attribute] - ave[attribute]) / std[attribute]

standardize_variable(df3)

print(df.head)
print(df2.head)
print(df3.head)