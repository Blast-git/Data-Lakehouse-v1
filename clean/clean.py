import json
import pandas as pd
import os

symbol = "IBM"

with open("../bronze/IBM-2026-06-18.json") as f:
    raw_data = json.load(f)

df = pd.DataFrame.from_dict(
    raw_data["Monthly Time Series"],
    orient="index"
)

df.reset_index(inplace=True)

df.rename(columns={
    "index": "date",
    "1. open": "open",
    "2. high": "high",
    "3. low": "low",
    "4. close": "close",
    "5. volume": "volume"
}, inplace=True)

df["symbol"] = symbol

df["date"] = pd.to_datetime(df["date"])

for col in ["open", "high", "low", "close"]:
    df[col] = df[col].astype(float)

df["volume"] = df["volume"].astype(int)

df.sort_values("date", inplace=True)

os.makedirs("../silver", exist_ok=True)

df.to_parquet("../silver/ibm.parquet")  