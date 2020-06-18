import yfinance as yf
import streamlit as st

st.write("""
Shown are the stocks closing price and volume of Google!
""")

tickerSymbol = 'GOOGL'

tickerData = yf.Ticker(tickerSymbol)
tickerDf = tickerData.history(period='1d', start='2010-5-31', end='2020-6-17')

st.line_chart(tickerDf.Close)
st.line_chart(tickerDf.Volume)