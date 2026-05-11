import numpy as np


def generate_forecast(prices):

    prices = prices.dropna()

    historical = prices.tail(30).tolist()

    # Simple AI-style trend continuation

    returns = prices.pct_change().dropna()

    avg_return = returns.mean()

    last_price = historical[-1]

    forecast = []

    current = last_price

    for _ in range(10):

        noise = np.random.normal(
            avg_return,
            0.01
        )

        current = current * (1 + noise)

        forecast.append(float(current))

    return {

        "historical":
            historical,

        "forecast":
            forecast
    }