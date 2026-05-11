from fastapi import APIRouter, Query

from app.services.data_service import fetch_stock_data
from app.services.forecast_service import generate_forecast

router = APIRouter()


@router.get("/forecast")
def forecast_stock(

    ticker: str = Query(...)

):

    data = fetch_stock_data([ticker])

    prices = data["price_data"][ticker]

    forecast = generate_forecast(prices)

    return forecast