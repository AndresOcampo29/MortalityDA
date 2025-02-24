import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

from Cleaning.cleaning import cleaning

file_path = 'WHOMortalityDatabase.csv'

df = pd.read_csv(file_path, skiprows=6, index_col=False)


# Data filtering by Colombia
df = df[df['Country Name'] == 'Colombia']

df = cleaning(df)

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
