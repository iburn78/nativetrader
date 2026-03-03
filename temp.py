#%%
import yfinance as yf

krb = yf.Ticker("005930.KS")
a = krb.history(period="1y")
print(a)
a.plot()
#%% 
a['Close'].plot()
#%% 

import FinanceDataReader as fdr
fdr.DataReader('005930', start='2025-03-01')
#%%
print(a['Close'][-50:])
