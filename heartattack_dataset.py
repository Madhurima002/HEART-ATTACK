#!/usr/bin/env python
# coding: utf-8

# In[1]:


pip install opendatasets


# In[2]:


import opendatasets as od


# In[3]:


dataset='https://www.kaggle.com/datasets/pritsheta/heart-attack'


# In[4]:


od.download(dataset)


# In[5]:


import os


# In[9]:


data_dir='.\heart-attack'


# In[10]:


os.listdir(data_dir)


# In[11]:


os.listdir(data_dir)


# In[12]:


import pandas as pd


# In[14]:


life_df= pd.read_csv('Heart Attack Data Set.csv')


# In[19]:


life_df= pd.read_csv('Heart Attack Data Set.csv')
life_df


# In[ ]:





# In[ ]:




