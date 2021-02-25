import pandas as pd
import yfinance as yf
import numpy as np
import datetime as dt


def macd(df1,a,b,c):
    df1['MA_Fast']=df1['Adj Close'].ewm(span=a,min_periods=a).mean()
    df1['MA_Slow']=df1['Adj Close'].ewm(span=b,min_periods=b).mean()
    df1['MACD']=df1['MA_Fast']-df1['MA_Slow']
    df1['Signal']=df1['MACD'].ewm(span=c,min_periods=c).mean()
    #print(df1)
    df1.dropna(inplace=True)

    return df1.iloc[:,[5,6,7,8,9]]
ticker = "AAPL"
ohlcv = yf.download(ticker,dt.date.today()-dt.timedelta(1825),dt.datetime.today())
df2 = ohlcv
print(macd(df2,12,26,9))
