import { useEffect, useState } from "react";
import axios from "axios";

import {
  PieChart, Pie, Cell, Tooltip, Legend,
  LineChart, Line, XAxis, YAxis,
  AreaChart, Area
} from "recharts";

const API = import.meta.env.VITE_API_URL;

function App() {

  const [classical, setClassical] = useState(null);
  const [quantum, setQuantum] = useState(null);
  const [predictedReturns, setPredictedReturns] = useState([]);
  const [forecastData, setForecastData] = useState(null);
  const [backtest, setBacktest] = useState([]);
  const [risk, setRisk] = useState(null);
  const [comparison, setComparison] = useState(null);

  const [inputTickers, setInputTickers] =
    useState("AAPL,MSFT,GOOGL");

  const [stocks, setStocks] =
    useState(["AAPL", "MSFT", "GOOGL"]);

  const fetchData = async () => {

    const tickers = inputTickers;

    const tickerArray = tickers.split(",").map(t => t.trim());

    setStocks(tickerArray);

    const classicalRes = await axios.get(`${API}/optimize-classical?tickers=${tickers}`);
    const quantumRes = await axios.get(`${API}/optimize-quantum?tickers=${tickers}`);
    const forecastRes = await axios.get(`${API}/forecast?ticker=${tickerArray[0]}`);
    const backtestRes = await axios.get(`${API}/backtest?tickers=${tickers}`);
    const riskRes = await axios.get(`${API}/risk`);

    setClassical(classicalRes.data.best_portfolio);
    setQuantum(quantumRes.data);
    setPredictedReturns(classicalRes.data.predicted_returns);
    setForecastData(forecastRes.data);
    setBacktest(backtestRes.data.portfolio_values);
    setRisk(riskRes.data);

    setComparison([
      {
        name: "Classical",
        return: classicalRes.data.best_portfolio.return,
        risk: classicalRes.data.best_portfolio.risk,
        sharpe: classicalRes.data.best_portfolio.sharpe
      },
      {
        name: "Quantum",
        return: quantumRes.data.expected_return,
        risk: 0.01,
        sharpe: quantumRes.data.expected_return / 0.01
      }
    ]);
  };

  useEffect(() => {
    fetchData();
  }, []);

  const backtestData = backtest.map((v, i) => ({
    day: i,
    value: v
  }));

  return (
    <div className="min-h-screen bg-black text-white p-10">

      <h1 className="text-4xl mb-6">
        Quantum AI Portfolio Optimizer
      </h1>

      <input
        className="bg-gray-800 p-3 w-full"
        value={inputTickers}
        onChange={(e) => setInputTickers(e.target.value)}
      />

      <button
        className="bg-cyan-500 px-4 py-2 mt-4"
        onClick={fetchData}
      >
        Run
      </button>

      {/* STRATEGY COMPARISON */}
      {comparison && (
        <div className="mt-10">

          <h2>Strategy Comparison</h2>

          <table className="w-full border">

            <thead>
              <tr>
                <th>Strategy</th>
                <th>Return</th>
                <th>Risk</th>
                <th>Sharpe</th>
              </tr>
            </thead>

            <tbody>
              {comparison.map((c, i) => (
                <tr key={i}>
                  <td>{c.name}</td>
                  <td>{c.return.toFixed(4)}</td>
                  <td>{c.risk.toFixed(4)}</td>
                  <td>{c.sharpe.toFixed(4)}</td>
                </tr>
              ))}
            </tbody>

          </table>

        </div>
      )}

      {/* RISK */}
      {risk && (
        <div className="mt-10 bg-gray-900 p-4">

          <h2>Risk Metrics</h2>

          <p>VaR 95%: {risk.VaR_95.toFixed(4)}</p>
          <p>Max Drawdown: {risk.max_drawdown.toFixed(4)}</p>

        </div>
      )}

      {/* BACKTEST */}
      {backtest.length > 0 && (
        <div className="mt-10">

          <h2>Backtest</h2>

          <AreaChart width={800} height={300} data={backtestData}>
            <XAxis dataKey="day" />
            <YAxis />
            <Tooltip />
            <Area dataKey="value" stroke="#00ff88" />
          </AreaChart>

        </div>
      )}

      {/* REPORT BUTTON */}
      <button
        className="bg-green-500 px-4 py-2 mt-10"
        onClick={() => window.open(`${API}/report`, "_blank")}
      >
        Download Report
      </button>

    </div>
  );
}

export default App;