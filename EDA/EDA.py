import matplotlib.pyplot as plt
import seaborn as sns
from pandas import DataFrame


def plot_death_rate(df: DataFrame):
    # Death rate per 100 000 population by year
    plt.figure(figsize=(12, 6))
    sns.lineplot(data=df, x='Year',
                 y='Death rate per 100 000 population')
    plt.title('Death rate per 100 000 population by year in Colombia')
    plt.show()
