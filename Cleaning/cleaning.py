from pandas import DataFrame
import pandas as pd


def cleaning(data: DataFrame):
    # Data Cleaning
    # Erease unnecessary columns
    data = data.drop(columns=['Region Code', 'Country Code', 'Age group code',
                              'Percentage of cause-specific deaths out of total deaths',
                              'Age-standardized death rate per 100 000 standard population'])

    # Column formatting
    data['Number'] = pd.to_numeric(data['Number'], errors='coerce')
    data['Death rate per 100 000 population'] = pd.to_numeric(
        data['Death rate per 100 000 population'], errors='coerce')

    # Filling null values with column mean
    means = data[['Number', 'Death rate per 100 000 population']].mean()
    data['Number'] = data['Number'].fillna(means['Number'])
    data['Death rate per 100 000 population'] = data['Death rate per 100 000 population'].fillna(
        means['Death rate per 100 000 population'])

    return data
