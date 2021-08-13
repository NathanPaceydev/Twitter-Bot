#!/usr/bin/env python
# coding: utf-8

# ### Script to Scrape BTC from Yahoo
# #### Tutorial: https://realpython.com/beautiful-soup-web-scraper-python/

# In[4]:


# import libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np


# ## Program that scrapes BTC to CAD usings div addresses

# In[3]:


URL = "https://ca.finance.yahoo.com/quote/BTC-CAD/"
page = requests.get(URL)
soup = BeautifulSoup(page.text, "html.parser")
#print(page.text)

results = soup.find(id="quote-header-info") # start with the main div id class
#print(results.prettify()) # ------------------> test that the site was extracted correctly
#print(results.text.strip()) #extract the text
#print(results.div) #extract the next div deep to test

# time to go deeper into the divs and extract the one we want
# next div deep 1
resDiv1 = soup.find("div",class_ = "D(ib) smartphone_Mb(10px) W(70%) W(100%)--mobp smartphone_Mt(6px)")
#print(resDiv1.prettify())

#next div deep 2
resDiv1_1 = soup.find("div",class_ = "D(ib) Va(m) Maw(65%) Ov(h)")
#print(resDiv1_1.prettify())

#next div deep 3
resDiv1_1_1 = soup.find("div",class_ = "D(ib) Mend(20px)")
#print(resDiv1_1_1.prettify())

#last div deep 4, with the BTC price
BTC_Price = resDiv1_1_1.find("span", class_="Trsdu(0.3s) Fw(b) Fz(36px) Mb(-4px) D(ib)")

BTCString = "Current CAD for one BTC "+str(BTC_Price.text.strip())
print(BTCString) # print the text


# In[ ]:




