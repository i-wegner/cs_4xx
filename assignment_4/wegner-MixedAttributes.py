import numpy as np
import pandas as pd

df = pd.read_csv('mixed_data.csv')

def rank_transform(series): # rank transformation and normilization for nonlinear attribute(s)
    series = series.rank(method = 'dense')
    s_min = series.min()
    s_max = series.max()

    if s_min == s_max:
        return series

    else:
        series = (series - s_min) / (s_max - s_min)

    return series

def normalize_variable(series): # normalize linear variable(s)
    s_min = series.min()
    s_max = series.max()

    if s_min == s_max:
        return series

    else:
        series = (series - s_min) / (s_max - s_min)

    return series