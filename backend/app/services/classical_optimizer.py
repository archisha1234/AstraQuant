import numpy as np


def simulate_portfolios(

    mean_returns,
    covariance_matrix,
    num_portfolios=5000

):

    results = []

    num_assets = len(mean_returns)

    for _ in range(num_portfolios):

        weights = np.random.random(num_assets)

        weights /= np.sum(weights)

        portfolio_return = np.dot(
            weights,
            mean_returns
        )

        portfolio_risk = np.sqrt(

            np.dot(
                weights.T,

                np.dot(
                    covariance_matrix,
                    weights
                )
            )
        )

        sharpe_ratio = (
            portfolio_return /
            portfolio_risk
        )

        results.append({

            "return":
                float(portfolio_return),

            "risk":
                float(portfolio_risk),

            "sharpe":
                float(sharpe_ratio),

            "weights":
                weights.tolist()
        })

    best_portfolio = max(
        results,
        key=lambda x: x["sharpe"]
    )

    return {

        "best_portfolio":
            best_portfolio,

        "all_portfolios":
            results
    }