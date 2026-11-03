import numpy as np
import pandas as pd

df = pd.read_csv('mixed_data.csv')
norm_df = df.copy()

ranking = df['Ranking']
h = len(ranking.drop_duplicates())

def rank_transform(series):
    series = np.log(series)
    return series

def normalize_variable(df):
    # could generalize this with:
    # series_dict = {col: df[col] for col in df.columns()}
        # this creates a dictionary with each column title as the key, but I don't know how to 
        # identify the data type for normalization within the program, thus   
    wage = df['MedianWage']
    ranking = df['Ranking'].astype(float)
    num_employees = df['NumberOfEmployees'] # how to tell if nonlinear???
    mental_support = df['MentalHealthSupport']
    industry = df['Industry']

    h = len(ranking.drop_duplicates())

    rank_transform(num_employees)

    for i in range(len(df)):
        ranking[i] = (ranking[i] - 1) / (h - 1)
        wage[i] = (wage[i] - wage.min()) / (wage.max() - wage.min())
        num_employees[i] = (num_employees[i] - num_employees.min()) / (num_employees.max() - num_employees.min())
        pass
    pass

normalize_variable(df)

# wage - ratio
# ranking - ordinal
# num_emp - ratio
# support - 
# industry - nominal