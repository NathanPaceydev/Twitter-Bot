#!/usr/bin/env python
# coding: utf-8

# ## Program to Tweet BTC and ETH
# #### Twitter API Tutorial: https://realpython.com/twitter-bot-python-tweepy/
# #### Yahoo Finance API Tutorial: https://towardsdatascience.com/how-to-get-stock-data-using-python-c0de1df17e75
# #### Twitter Bot: https://twitter.com/NathanPaceyBot
# 
# ###### Where to find user ID's: https://tweeterid.com/

# In[1]:


import tweepy
import yfinance as yf
import time
import numpy as np

# Authenticate to Twitter
#consumer API key, API secret key
auth = tweepy.OAuthHandler("baRbsry9xKBUePSqYjaAPTMYe", 
    "6TueT7Quu822ADmcNodsCR312cBB5F5uOjKC2qhh40IIBvKnJf")

#Access token
auth.set_access_token("1425121753316184073-lbLeZefImj38n6CacOtf7JRjQvyRc9", 
    "aHJO3Lc8Q0pgVlXdhtav97ZtoJ2ezNJBAGt1vfTnXjBsq")

api = tweepy.API(auth)

try:
    api.verify_credentials()
    print("Authentication OK")
except:
    print("Error during authentication")


# ## Changing Profile description
#Changing my profile description
api.update_profile(description="Twitter Bot - Designed By Nathan Pacey (@nathanpacey01)")
# ## Tweeting Text
#code to tweet strings
api.update_status("Sending BTC and ETH updates twice a day, at noon and midnight EST")
# ## Direct Message me

# In[2]:


#my personal Twitter ID
myTwitterID =  2832211566

#The Bots twitter ID
TwitterBotID = 1425121753316184073

#direct message command
api.send_direct_message(myTwitterID, "Hey Nathan are you having fun yet?")


# #### Messaging My Girlfriend
# This is just a little joke
#My Girlfriends twitter ID
GirlfriendsID = 2384404691

MeganString = "Hi just a reminder I love you - sent by a Bot"
api.send_direct_message(GirlfriendsID, MeganString)

ThisMuch = "<3 "
#direct message command
while(1):
    ThisMuch+=ThisMuch
    api.send_direct_message(GirlfriendsID, ThisMuch)
# ### Sending BTC Updates every 30 minutes

# In[3]:



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

# function to get ETH data
def getETHdata():
    ETH_to_CAD = 'ETH-CAD'
    #get data on this ticker
    ETH_to_CAD_Data = yf.Ticker(ETH_to_CAD)
    return ETH_to_CAD_Data


def getETHPrice():
    #get data on this ticker
    ETH_to_CAD_Data = getETHdata()

    price = ETH_to_CAD_Data.info['regularMarketPrice']
    
    #print(price) # can comment this out depending on preference
    return price




# In[4]:


#the change of the price since yesterday
def getBTCDailyChange():
    BTC_to_CAD_Data = getBTCdata()
    priceCurr = float(getBTCPrice())
    print(priceCurr)
    priceYesterday = float(BTC_to_CAD_Data.info['regularMarketPreviousClose'])
    #print(priceCurr)
    #print(priceYesterday)
    diff = priceCurr-priceYesterday
    #print(diff)
    return diff

getBTCDailyChange()

#the change of the price since today's high
def getBTCDailyUpDown():
    BTC_to_CAD_Data = getBTCdata()
    dayHigh = BTC_to_CAD_Data.info['dayHigh']
    priceCurr = getBTCPrice()
    change = priceCurr - dayHigh
    #print(change)
    
    return change

getBTCDailyUpDown()

def getBTCDailyChangePercent():
    diff = getBTCDailyChange()
    price = getBTCPrice()
    return diff/price*100



## ETH Versions

#the change of the price since yesterday
def getETHDailyChange():
    ETH_to_CAD_Data = getETHdata()
    priceCurr = getETHPrice()
    priceYesterday = ETH_to_CAD_Data.info['regularMarketPreviousClose']
    #print(priceCurr)
    #print(priceYesterday)
    diff = priceCurr-priceYesterday
    #print(diff)
    return diff

getETHDailyChange()

#the change of the price since today's high
def getETHDailyUpDown():
    ETH_to_CAD_Data = getETHdata()
    dayHigh = ETH_to_CAD_Data.info['dayHigh']
    priceCurr = getETHPrice()
    change = priceCurr - dayHigh
    #print(change)
    
    return change

getETHDailyUpDown()

def getETHDailyChangePercent():
    diff = getETHDailyChange()
    price = getETHPrice()
    return diff/price*100

#print(str(round(getETHDailyChangePercent(),3))+"%")


# In[5]:


# function that calculates how much CAD I have in BTC
def myBTCworth(price):
    amountBTC = 0.04016036
    amountCAD = price*amountBTC
    return amountCAD

def myETHworth(ethPrice):
    amountETH = 0.172
    amountETH = ethPrice*amountETH
    return amountETH


# In[6]:


# import library for the time of day
from datetime import datetime, date, timezone
import time

    
# make a function to send the BTC price
def tweet_check():
    
    price_BTC = round(getBTCPrice(),2) #call the BTC func and get the price
    amountCAD_BTC = round(myBTCworth(price_BTC),2)
    
    price_ETH = round(getETHPrice(),2) #call the ETH func and get the price
    amountCAD_ETH = round(myETHworth(price_ETH),2)
    
    # create two seperate strings one for the feed and one for dm's
    BTC_Tweet_String = "The Current CAD for one BTC is $" + str(price_BTC)
    BTC_DM_String = "The Current CAD for one BTC is $" + str(price_BTC) +"\n\nYou own $"+str(amountCAD_BTC)+" CAD in BTC\n"
    
    api.send_direct_message(myTwitterID, BTC_DM_String) #message me my BTC worth
    api.update_status(BTC_Tweet_String) #tweet the BTC overall worth
    
    
    # create two seperate strings one for the feed and one for dm's
    ETH_Tweet_String = "The Current CAD for one ETH is $" + str(price_ETH)
    ETH_DM_String = "The Current CAD for one ETH is $" + str(price_ETH) +"\n\nYou own $"+str(amountCAD_ETH)+" CAD in ETH\n"
    
    api.send_direct_message(myTwitterID, ETH_DM_String) #message me my ETH worth
    api.update_status(ETH_Tweet_String) #tweet the overall ETH worth
    
    #DM my net Worth
    NetWorthSTr = "\nCurrent Net Worth:\n"+str(round((amountCAD_BTC+amountCAD_ETH),2))
    api.send_direct_message(myTwitterID, NetWorthSTr) #message me my NET worth
    
    if(price_BTC > 77000): # seperate message if BTC hits a HIGH
        # create two seperate strings one for the feed and one for dm's
        BTC_Tweet_String = "Bitcoin is hitting a HIGH!!!\nThe Current CAD for one BTC is $" + str(price_BTC)
        BTC_DM_String = "Bitcoin is hitting a HIGH!!!\nThe Current CAD for one BTC is $" + str(price_BTC) +"\n\nYou own $"+str(amountCAD_BTC)+" CAD in BTC\n"

        api.send_direct_message(myTwitterID, BTC_DM_String) #message me my BTC worth
        api.update_status(BTC_Tweet_String) #tweet the BTC overall worth
        return
    
    time.sleep(60) #set the timer to 1 min
    
#tweet_check end

def tweetChange(token,percent):
    DM_String = str(token)+" has changed by "+str(round(percent,2))+ "% since yesterday"
    api.send_direct_message(myTwitterID, DM_String) #message me my BTC worth
    api.update_status(DM_String) #tweet the BTC overall worth
#tweetChange end


# In[7]:


#tweet_check()

# repeat and call the function in the main driver
if __name__ == '__main__':
    # This would be how it constantly runs the check
    
    while True:
        dateTime = str(datetime.now().isoformat(timespec='minutes')) #timeZone GMT +/-0
        Hours =  dateTime[-5:]
        BTCDailyChange = getBTCDailyChangePercent()
        ETHDailyChange = getETHDailyChangePercent()

        if (Hours == "04:00") or (Hours == "16:00"):
            if(abs(BTCDailyChange)>5):
                tweetChange("ETH",ETHDailyChange)
        
            if(abs(ETHDailyChange)>5):
                tweetChange("BTC",BTCDailyChange)
                
            tweet_check() #call tweet func

