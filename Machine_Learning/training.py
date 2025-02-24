import pandas as pd
from pandas import DataFrame
from sklearn.preprocessing import MinMaxScaler
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error


def training_model(df: DataFrame) -> RandomForestRegressor:
    # Splitting the dataset
    X = df[['Year', 'Number']]
    y = df['Death rate per 100 000 population']

    # Splitting the dataset into training and testing
    X_train = X[X['Year'] < 2016]
    X_test = X[X['Year'] >= 2016]
    y_train = y[X['Year'] < 2016]
    y_test = y[X['Year'] >= 2016]

    # Normalizing the data
    min_max_scaler = MinMaxScaler()
    X_train_scaled = min_max_scaler.fit_transform(X_train)
    X_test_scaled = min_max_scaler.transform(X_test)

    # Training the model
    model = RandomForestRegressor(n_estimators=100, random_state=42)
    model.fit(X_train_scaled, y_train)

    # Predicting the test set
    y_pred = model.predict(X_test_scaled)

    # Evaluating the model
    mae = mean_absolute_error(y_test, y_pred)
    mse = mean_squared_error(y_test, y_pred)
    rmse = mse ** 0.5

    print(f"MAE: {mae}, RMSE: {rmse}")
