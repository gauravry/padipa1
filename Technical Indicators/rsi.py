import pandas as pd
import yfinance as yf
import numpy as np
import datetime as dt




df2 = pd.DataFrame({'col1':[33,36,13,14,16,28,32,31,36,11,11,22,16,29,24,29,15,22,26,14,18,31,34,22,35,14,18,32,11,14,]})
df2['delta'] = df2-df2.shift(1)

df2['gain']=df2['delta'].apply(lambda x: x if x > 0 else 0)
df2['loss']=df2['delta'].apply(lambda x: -x if x < 0 else 0)
avg_gain=[]
avg_loss=[]
n=3
for i in range(len(df2)):
    if i < n:
        avg_gain.append(np.NaN)
        avg_loss.append(np.NaN)

    elif (i == n):
        avg_gain.append(df2['gain'].rolling(n).mean().tolist()[n])
        avg_loss.append(df2['loss'].rolling(n).mean().tolist()[n])
    elif i > n:
        avg_gain.append(((n-1)*avg_gain[i-1] + df2['gain'][i])/n)
        avg_loss.append(((n-1)*avg_loss[i-1] + df2['loss'][i])/n)


# df2['loss']=df2[df2['delta']<0]
df2.dropna(inplace=True)

print(df2)
df2['avg_gain']=pd.Series(avg_gain)
df2['avg_loss']=pd.Series(avg_loss)
df2['RS']=df2['avg_gain']/df2['avg_loss']
df2['RSI']=100-(100/(1+df2['RS']))
print(df2.dropna(inplace=True))
print(df2)
