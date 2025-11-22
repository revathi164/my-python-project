from fastapi import FastAPI
import yfinance as yf
import pandas as pd

app = FastAPI()

@app.get("/")
def root():
    return {"status": "API working"}

@app.get("/stock")
def get_stock(symbol: str = "AAPL"):
    # download data
    df = yf.download(symbol, period="1mo")

    # Reset index (Date column)
    df = df.reset_index()

    # Convert Timestamp → string
    df["Date"] = df["Date"].astype(str)

    # Convert all numpy values → Python native types
    df = df.applymap(lambda x: x.item() if hasattr(x, "item") else x)

    # Convert DataFrame to list of dictionaries
    result = df.to_dict(orient="records")

    return result
