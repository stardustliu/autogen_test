# filename: ytd_comparison.py
import yfinance as yf
from datetime import datetime

# Define the tickers for META and TESLA
tickers = ["META", "TSLA"]

# Define the start and end dates for YTD calculation
start_date = "2024-01-01"
end_date = "2024-02-05"  # Today's date

# Function to calculate YTD gain
def calculate_ytd_gain(ticker):
    stock = yf.Ticker(ticker)
    hist = stock.history(start=start_date, end=end_date)
    # Get the opening price of the first trading day of the year and the latest closing price
    opening_price = hist.iloc[0]['Open']
    closing_price = hist.iloc[-1]['Close']
    ytd_gain = ((closing_price - opening_price) / opening_price) * 100
    return ytd_gain

# Calculate and print YTD gains
for ticker in tickers:
    ytd_gain = calculate_ytd_gain(ticker)
    print(f"{ticker} YTD Gain: {ytd_gain:.2f}%")
