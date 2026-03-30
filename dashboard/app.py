from sqlalchemy import create_engine
from dotenv import load_dotenv
import plotly.express as px
import streamlit as st
import pandas as pd 
import os

load_dotenv()

# Connecting to Supabase
engine = create_engine(os.getenv("DATABASE_URL"))

# Read data
df = pd.read_sql("SELECT * FROM stock_prices", engine)

# Streamlite.title 
st.title("AAPL")

# Show graf
fig = px.line(df, x="date", y="close")
st.plotly_chart(fig)