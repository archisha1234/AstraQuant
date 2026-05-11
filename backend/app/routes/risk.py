from fastapi import APIRouter
import numpy as np
import yfinance as yf

router = APIRouter()


def compute_risk(returns):

    returns = np.array(returns)

    var_95 = np.percentile(returns, 5)

    cumulative = np.cumprod(1 + returns)

    peak = np.maximum.accumulate(cumulative)

    drawdown = (cumulative - peak) / peak

    max_drawdown = np.min(drawdown)

    return {
        "VaR_95": float(var_95),
        "max_drawdown": float(max_drawdown)
    }


@router.get("/risk")
def risk():

    data = yf.download("AAPL", period="6mo")["Close"]

    returns = data.pct_change().dropna()

    return compute_risk(returns)