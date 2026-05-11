from fastapi import APIRouter
from app.services.data_service import fetch_stock_data

router = APIRouter()


@router.get("/market-data")
def get_market_data():

    tickers = ["AAPL", "MSFT", "GOOGL"]

    data = fetch_stock_data(tickers)

    return {
        "mean_returns": data["mean_returns"].to_dict()
    }