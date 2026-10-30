import numpy as np
import pandas as pd

df = pd.read_csv('mixed_data.csv')

ranking = df['Ranking']
h = len(ranking.drop_duplicates())

def normalize_variable(df):
    # could generalize this with:
    # series_dict = {col: df[col] for col in df.columns()}
        # this creates a dictionary with each column title as the key, but I don't know how to 
        # identify the data type for normalization within the program, thus   
    wage = df['MedianWage']
    ranking = df['Ranking']
    num_employees = df['NumberOfEmployees']
    mental_support = df['MentalHealthSupport']
    industry = df['Industry']

    h = len(ranking.drop_duplicates())

    for i in range(len(df)):
        ranking[i] - 1
        
        pass
    pass

def rank_transform():
    pass

# wage - ratio
# ranking - ordinal
# num_emp - ratio
# support - 
# industry - nominal