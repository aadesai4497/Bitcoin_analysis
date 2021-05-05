#!/usr/bin/env python
# coding: utf-8

# In[1]:


import numpy as np
import pandas as pd
import os
import seaborn as sns


# In[2]:


print(os.listdir())


# In[3]:


df = pd.read_csv("https://bitcoin-project-data.s3.amazonaws.com/bitstampUSD_1-min_data_2012-01-01_to_2021-03-31.csv")


# In[4]:


df


# In[5]:


df.isnull().sum()


# In[6]:


df.dropna(inplace= True)


# In[ ]:


df.to_csv("/Users/abhishekdesai/Desktop/cloudproject/bitcoinout.csv")


# In[ ]:




