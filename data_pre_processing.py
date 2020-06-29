#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd


# In[2]:


nbr_trading_days = 252

#reading stock data
stocks_data_file_path = 'stocks.csv'
stocks_data = pd.read_csv(stocks_data_file_path)
stocks_data  = stocks_data.sort_values(['ticker', 'Date'])
print('stocks considered : ' + str(np.unique(stocks_data['ticker'])))


# In[3]:


pivot_table = pd.pivot_table(stocks_data, values='Close', index=['Date'],columns=['ticker'])
returns = pivot_table.pct_change().dropna()
stocks_returns_mean = returns.mean()
stocks_covariance_matrix = returns.cov()


# In[4]:


def get_input_data(data_table, ticker_column_name):
    open_values = list()
    close_values = list()
    high_values = list()
    low_values = list()

    for ticker in np.unique(data_table[ticker_column_name]):
        open_value_list = data_table['Open'].loc[data_table[ticker_column_name]==ticker]
        open_values.append(open_value_list[1:].reset_index(drop = True) / open_value_list[:-1].reset_index(drop = True))
        close_values.append(data_table['Close'].loc[data_table[ticker_column_name]==ticker][:-1] / open_value_list[:-1])
        high_values.append(data_table['High'].loc[data_table[ticker_column_name]==ticker][:-1] / open_value_list[:-1])
        low_values.append(data_table['Low'].loc[data_table[ticker_column_name]==ticker][:-1] / open_value_list[:-1])
    
    return np.array([close_values,
                     high_values,
                     low_values,
                     open_values])


# In[5]:


stocks_input_array = get_input_data(stocks_data, 'ticker')
np.save('stocks_data_input.npy', stocks_input_array)
print('shape of stocks data input : ' + str(stocks_input_array.shape))


# In[ ]:




