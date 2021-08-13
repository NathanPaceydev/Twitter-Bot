#!/usr/bin/env python
# coding: utf-8

# In[1]:


# import libraries
import pandas as pd
import requests
from bs4 import BeautifulSoup
import numpy as np


# ## Program to scrape the NASDAQ company listings

# In[8]:


URL = "https://www.advfn.com/nasdaq/nasdaq.asp"
page = requests.get(URL)
soup = BeautifulSoup(page.text, "html.parser")
#print(page.text)

# find every container tr with class ts0 and ts1
res1 = soup.find_all("tr", class_ = "ts0")
res2 = soup.find_all("tr", class_ = "ts1")

genList = []

for x,y in zip(res1,res2):
    list1 = [t.text for t in (x.find_all("td"))]
    genList.append(list1)
    list2 = [t.text for t in (y.find_all("td"))]
    genList.append(list2)

for i in genList:
    print(i)


#newList = str(genList).replace(',',"")
    
#print(newList[0:][0:])


# ### Now let's find some values  / attributes

# In[4]:



# function to print the highest share price
def MaxSharePrice(genList):
    newList = []

    for a in range(len(genList)):
        newList.append((genList[a][3]))
        newList[a] = newList[a].replace(",","")
    #print((newList))
    #print()
    
    prices = []
    
    for i in newList:
        #print(i[3])
        #genList = genList.replace("3,327.59","3327.59")
        prices.append(float((i)))

    #print(prices)    
    #print("\nThe index of max stock price "+str(np.argmax(prices)))
    print("The stock with the highest price per share: "+str(genList[np.argmax(newList)][0])+" with a stock price of $"+ str(genList[np.argmax(prices)][3]))
    print()
    
# function to find the largest Max change
def MaxChange(genList):
    change = []
    for i in genList:
        #print(i[3])
        change.append(abs(float((i[4]))))

    #print(prices)    
    #print("\nThe index of max stock price "+str(np.argmax(prices)))
    print("The stock with largest +/- : "+str(genList[np.argmax(change)][0])+" with a change of "+ str(genList[np.argmax(change)][4]))
    print()
    
def MaxPChange(genList):
    Percentchange = []
    for i in genList:
        Percentchange.append(abs(float((i[5][:-1]))))
    #print(Percentchange)    
    #print("\nThe index of max stock price "+str(np.argmax(prices)))
    print("The stock with largest % change: "+str(genList[np.argmax(Percentchange)][0])+" with a percentage change of "+ str(genList[np.argmax(Percentchange)][5]))
    print()  
    
    
    
    
MaxSharePrice(genList)    
MaxChange(genList)
MaxPChange(genList)


# In[ ]:




