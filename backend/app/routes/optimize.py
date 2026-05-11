from fastapi import APIRouter, Query

from app.services.data_service import fetch_stock_data
from app.services.classical_optimizer import simulate_portfolios
from app.services.ai_predictor import predict_future_returns

router = APIRouter()


@router.get("/optimize-classical")
def classical_optimization(

    tickers: str = Query(...)

):

    ticker_list = tickers.split(",")

    data = fetch_stock_data(ticker_list)

    predicted_returns = predict_future_returns(
        data["price_data"]
    )

    result = simulate_portfolios(
        predicted_returns,
        data["covariance_matrix"]
    )

    return {
        "best_portfolio":
            result["best_portfolio"],

        "all_portfolios":
            result["all_portfolios"],

        "predicted_returns":
            predicted_returns.tolist()
    }