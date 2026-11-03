import numpy as np
import pandas as pd

df = pd.read_csv('mixed_data.csv')

def rank_transform(df): # rank transformation and normilization for nonlinear attribute(s)
    num_emp = df['NumberOfEmployees']
    num_emp = num_emp.rank(method = 'dense')
    s_min = num_emp.min()
    s_max = num_emp.max()

    for i in range(len(num_emp)):
        num_emp[i] = (num_emp[i] - s_min) / (s_max - s_min)

    df['NumberOfEmployees'] = num_emp

def normalize_variable(df): # normalize linear variable(s)
    wage = df['MedianWage']
    ranking = df['Ranking'].astype(float)

    h = len(ranking.drop_duplicates())
    min_wage = wage.min()
    max_wage = wage.max()

    for i in range(len(df)):
        ranking[i] = (ranking[i] - 1) / (h - 1)
        wage[i] = (wage[i] - min_wage) / (max_wage - min_wage)

    df['Ranking'] = ranking
    df['MedianWage'] = wage