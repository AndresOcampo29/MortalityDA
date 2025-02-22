import pandas as pd

file_path = 'WHOMortalityDatabase.csv'

df = pd.read_csv(file_path, skiprows=6, index_col=False)
# First 5 rows
print(df.head())
# Info about the data
print(df.info())
# Check for missing values
print(df.isnull().sum())

# Data Cleaning
# Erease unnecessary columns
df = df.drop(columns=['Region Code', 'Country Code'])

# Column formatting
df['Number'] = pd.to_numeric(df['Number'], errors='coerce')
df['Death rate per 100 000 population'] = pd.to_numeric(
    df['Death rate per 100 000 population'], errors='coerce')

# Filling null values with column mean
means = df[['Number', 'Death rate per 100 000 population']].mean()
df['Number'] = df['Number'].fillna(means['Number'])
df['Death rate per 100 000 population'] = df['Death rate per 100 000 population'].fillna(
    means['Death rate per 100 000 population'])

print(df.isnull().sum())
