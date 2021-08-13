#!/usr/bin/env python
# coding: utf-8

# In[14]:


from datetime import datetime, date, timezone

print(time.hour)
#note EST is 3 hours behind GMT
dateTime = str(datetime.now().isoformat(timespec='minutes')) #timeZone GMT +/-0

print(dateTime)
Hours =  dateTime[-5:]

print(dateTime[-5:])

if(Hours == "01:31"):
    print("its 1:31")


# In[ ]:





# In[ ]:




