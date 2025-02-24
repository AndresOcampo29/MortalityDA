import pandas as pd

from Cleaning.cleaning import cleaning
from EDA.EDA import plot_death_rate
from Machine_Learning.training import training_model

file_path = 'WHOMortalityDatabase.csv'

df = pd.read_csv(file_path, skiprows=6, index_col=False)


# Data filtering by Colombia
df = df[df['Country Name'] == 'Colombia']

df = cleaning(df)

# Exploratory Analysis
plot_death_rate(df)

# Training the model
training_model(df)
