from fastapi import APIRouter, Query

from app.services.data_service import fetch_stock_data
from app.services.quantum_optimizer import quantum_optimize

router = APIRouter()


@router.get("/optimize-quantum")
def optimize_quantum(

    tickers: str = Query(...)

):

    ticker_list = tickers.split(",")

    data = fetch_stock_data(ticker_list)

    result = quantum_optimize(
        data["mean_returns"]
    )

    return result