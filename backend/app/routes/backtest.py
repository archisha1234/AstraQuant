from fastapi import APIRouter, Query

from app.services.data_service import fetch_stock_data
from app.services.classical_optimizer import simulate_portfolios
from app.services.ai_predictor import predict_future_returns

import numpy as np

router = APIRouter()


@router.get("/backtest")
def backtest(tickers: str = Query(...)):

    ticker_list = tickers.split(",")

    data = fetch_stock_data(ticker_list)

    prices = data["price_data"]

    predicted = predict_future_returns(prices)

    # simulate weights
    result = simulate_portfolios(
        predicted,
        data["covariance_matrix"],
        num_portfolios=1000
    )

    best = result["best_portfolio"]["weights"]

    # simulate growth
    returns = data["returns"]

    portfolio_values = [100]

    for i in range(len(returns)):

        daily_return = np.dot(
            returns.iloc[i].values,
            best
        )

        portfolio_values.append(
            portfolio_values[-1] *
            (1 + daily_return)
        )

    return {
        "portfolio_values": portfolio_values
    }