#!/usr/bin/env python
# coding: utf-8

# ### Yahoo API

# In[1]:


import yfinance as yf
import time


# ### Testing the API data for Microsoft

# In[2]:


#define the ticker symbol
tickerSymbol = 'MSFT'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2020-1-25')

#see your data
tickerDf


# ### Getting BTC to CAD data

# In[3]:


#define the ticker symbol
tickerSymbol = 'BTC-CAD'

#get data on this ticker
tickerData = yf.Ticker(tickerSymbol)

#get the historical prices for this ticker
tickerDf = tickerData.history(period='1d', start='2010-1-1', end='2021-8-12')

#see your data
tickerDf


# In[4]:


tickerData.info


# ### Now Creating a Function to output the BTC to CAD price

# In[9]:


# function to get BTC data
def getBTCdata():
    BTC_to_CAD = 'BTC-CAD'
    #get data on this ticker
    BTC_to_CAD_Data = yf.Ticker(BTC_to_CAD)
    return BTC_to_CAD_Data


def getBTCPrice():
    #get data on this ticker
    BTC_to_CAD_Data = getBTCdata()

    price = BTC_to_CAD_Data.info['regularMarketPrice']
    
    #print(price) # can comment this out depending on preference
    return price



# output the price every 20 seconds

getBTCPrice()
   


# In[20]:


BTC_to_CAD = 'BTC-CAD'

#the change of the price since yesterday
def getDailyChange():
    BTC_to_CAD_Data = getBTCdata()
    priceCurr = getBTCPrice()
    priceYesterday = BTC_to_CAD_Data.info['regularMarketPreviousClose']
    #print(priceCurr)
    #print(priceYesterday)
    diff = priceCurr-priceYesterday
    #print(diff)
    return diff

getDailyChange()

#the change of the price since today's high
def getDailyUpDown():
    BTC_to_CAD_Data = getBTCdata()
    dayHigh = BTC_to_CAD_Data.info['dayHigh']
    priceCurr = getBTCPrice()
    change = priceCurr - dayHigh
    #print(change)
    
    return change

getDailyUpDown()

def getDailyChangePercent():
    diff = getDailyChange()
    price = getBTCPrice()
    return diff/price*100

print(str(round(getDailyChangePercent(),3))+"%")


# In[ ]:




