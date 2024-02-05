# filename: plot_stock_price_ytd.py
import yfinance as yf
import matplotlib.pyplot as plt

# Define the tickers and fetch data
tickers = ["META", "TSLA"]
start_date = "2024-01-01"
end_date = "2024-02-05"  # Adjust to the current date if necessary

# Fetch stock data
data = yf.download(tickers, start=start_date, end=end_date)

# Plotting
plt.figure(figsize=(14, 7))
for ticker in tickers:
    plt.plot(data['Close'][ticker], label=ticker)

plt.title('Stock Price Change YTD')
plt.xlabel('Date')
plt.ylabel('Closing Price (USD)')
plt.legend()
plt.grid(True)

# Save the plot to a file
plt.savefig('stock_price_ytd.png')
plt.show()