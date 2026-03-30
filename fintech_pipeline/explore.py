import requests 
import os
from dotenv import load_dotenv
import pandas as pd
from sqlalchemy import create_engine

"""
Creates a dict which we can use to create a pandas DataFrame later on
"""
load_dotenv() 

api_key = os.getenv("ALPHAVANTAGE_API_KEY")

url = "https://www.alphavantage.co/query"
params = {
    "function": "TIME_SERIES_DAILY",
    "symbol": "AAPL",
    "intercal": "5min",
    "apikey": api_key
}

response = requests.get(url, params=params)
data = response.json()



"""
Crates Pandas DataFrame
"""
time_series = data["Time Series (Daily)"]
df = pd.DataFrame.from_dict(time_series, orient="index")

# Cleaning/renaiming 
df = df.rename(columns={"1. open": "open", "2. high": "high", "3. low": "low", "4. close": "close", "5. volume": "volume"})

# Rest index
df = df.reset_index(names=['date'])

# Add colum in pd.df
df["symbol"] = "AAPL"


"""
Save daataframe to supabase
"""
engine = create_engine(os.getenv("DATABASE_URL"))
df.to_sql("stock_prices", engine, if_exists="append", index=False)