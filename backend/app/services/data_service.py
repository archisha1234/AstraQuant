import yfinance as yf


def fetch_stock_data(tickers):

    data = yf.download(
        tickers,
        period="1y"
    )["Close"]

    returns = data.pct_change().dropna()

    mean_returns = returns.mean()

    covariance_matrix = returns.cov()

    return {

        "price_data": data,

        "returns": returns,

        "mean_returns": mean_returns,

        "covariance_matrix": covariance_matrix
    }