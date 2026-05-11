import numpy as np

from sklearn.ensemble import RandomForestRegressor


def predict_future_returns(price_data):

    predicted_returns = []

    for column in price_data.columns:

        prices = price_data[column]

        returns = prices.pct_change().dropna()

        # Create sequences
        X = []
        y = []

        window = 5

        for i in range(len(returns) - window):

            X.append(
                returns.iloc[i:i + window].values
            )

            y.append(
                returns.iloc[i + window]
            )

        X = np.array(X)
        y = np.array(y)

        # Small dataset protection
        if len(X) < 10:

            predicted_returns.append(
                float(returns.mean())
            )

            continue

        # Train model
        model = RandomForestRegressor(
            n_estimators=100,
            random_state=42
        )

        model.fit(X, y)

        # Predict next return
        latest_window = returns.iloc[-window:].values

        prediction = model.predict(
            [latest_window]
        )[0]

        predicted_returns.append(
            float(prediction)
        )

    return np.array(predicted_returns)