import pandas as pd
import numpy as np

df = pd.read_csv('cars-class.csv', header = None)
df = df.rename(columns={0:'Colour', 1:'Model'})

s_colour = df['Colour'].drop_duplicates() # create a pandas series with only the unique colours from df
s_model = df['Model'].drop_duplicates() # create a pandas series with only the unique models from df

num_colours = 0
colour_dict = {}

num_models = 0
model_dict = {}

for i in s_colour: # iterate over series
    colour_dict.update({num_colours : s_colour.iloc[num_colours]}) # add colour as value to dictionary paried with key = iteration #
    num_colours += 1 # increment num_colours by one
for i in s_model:
    model_dict.update({num_models : s_model.iloc[num_models]})
    num_models += 1

# instantiate a matrix (cube) with num_colours + 1 rows and num_models + 1 columns
# + for each so that we have the marginal row/column
cube = np.zeros((num_colours + 1, num_models + 1), dtype = int)

# iterate through df
# set temp_colour/model as program iterates through
# since keys are all unique and based on order that the colour/model was encounted in their respective series,
# reverse search the dictionary for the key associated with that value and use that key as the row/column for that colour/model
# use temp_row/column to index the cube and increment that model/colour combination by one
for i in range(df.shape[0]):
    temp_colour = df.iloc[i, 0]
    temp_model = df.iloc[i, 1]
    temp_row = next(key for key, value in colour_dict.items() if value == temp_colour)
    temp_column = next(key for key, value in model_dict.items() if value == temp_model)
    cube[temp_row][temp_column] += 1

for i in range(num_colours): # calculate marginal total for 
    cube[i][num_models] = cube[i].sum()
    print(f'{colour_dict[i]} cars: {cube[i][num_models]}')
for j in range(num_models):
    cube[num_colours][j] = np.sum(cube[:, j])
    print(f'{model_dict[j]} cars: {cube[num_colours][j]}')

cube[num_colours][num_models] = cube[num_colours].sum() # could also sum along the last column, but this syntax is more simple
print(f'The overall total number of cars sold: {cube[num_colours][num_models]}')