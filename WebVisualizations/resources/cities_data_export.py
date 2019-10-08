#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd


# In[2]:


df = pd.read_csv("resources/cities.csv")
df.to_html('resources/cities_data.html', index=False, classes='table')

