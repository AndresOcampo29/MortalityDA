import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns


file_path = 'WHOMortalityDatabase.csv'

df = pd.read_csv(file_path, skiprows=6, index_col=False)
# # First 5 rows
# print(df.head())
# # Info about the data
# print(df.info())
# # Check for missing values
# print(df.isnull().sum())

# Data filtering by Colombia
df = df[df['Country Name'] == 'Colombia']

# Data Cleaning
# Erease unnecessary columns
df = df.drop(columns=['Region Code', 'Country Code', 'Age group code',
             'Percentage of cause-specific deaths out of total deaths',
                      'Age-standardized death rate per 100 000 standard population'])

# Column formatting
df['Number'] = pd.to_numeric(df['Number'], errors='coerce')
df['Death rate per 100 000 population'] = pd.to_numeric(
    df['Death rate per 100 000 population'], errors='coerce')

# Filling null values with column mean
means = df[['Number', 'Death rate per 100 000 population']].mean()
df['Number'] = df['Number'].fillna(means['Number'])
df['Death rate per 100 000 population'] = df['Death rate per 100 000 population'].fillna(
    means['Death rate per 100 000 population'])


# Exploratory Analysis
# Statistic summary
print(df[['Number', 'Death rate per 100 000 population']].describe())
print(df.info())
# Death rate per 100 000 population by year
plt.figure(figsize=(12, 6))
sns.lineplot(data=df, x='Year',
             y='Death rate per 100 000 population')
plt.title('Death rate per 100 000 population by year in Colombia')
plt.show()
