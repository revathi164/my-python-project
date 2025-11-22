# import yfinance as yf
#
# symbol = ['AAPL',  "MSFT", "GOOGL"]
#
# data = yf.download(symbol, period='1mo')
#
# print(data)

import yfinance as yf

symbols = ["AAPL", "MSFT", "GOOGL"]

for sym in symbols:
    data = yf.download(sym, period="1mo")
    print(f"\nData for {sym}:\n")
    print(data)

import yfinance as yf
import matplotlib.pyplot as plt

# ---- Choose multiple stocks ----
# symbols = ["AAPL", "MSFT", "GOOGL"]      # USA
# symbols = ["RELIANCE.NS", "TCS.NS"]     # India
# symbols = ["VOD.L", "HSBA.L"]           # UK

# ---- Download data ----
# data = yf.download(symbols, period="6mo")['Close']

# ---- Plot ----
# plt.figure(figsize=(12, 6))
# for sym in symbols:
#     plt.plot(data.index, data[sym], label=sym)
#
# plt.title("Stock Price Comparison")
# plt.xlabel("Date")
# plt.ylabel("Closing Price")
# plt.legend()
# plt.grid(True)
# plt.show()

