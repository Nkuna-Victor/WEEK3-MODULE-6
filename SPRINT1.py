#!/usr/bin/env python
# coding: utf-8

# In[3]:


#Author:Victor Nkuna
#Created:29/03/2020

import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')



# In[4]:


dict_item={"Chips": ["Simba", "Lays"],"Cooldrinks": ["Coke", "Fanta"],"Chocolates": ["Cadbury", "Tex"],"Pies": ["Pepper Steak", "Chicken"],"Fruit": ["Pear", "Apple", "Orange"],"Cupcakes": ["vanilla", "chocolate"],"Veggies":["spinach", "cabbage"]}


# In[5]:



"""
-->this line of code will output errors of "ARRAY MUST BE OF SAME LENGTGH"

df=pd.DataFrame(dict_item)   -->this line of code will output errors of "ARRAY MUST BE OF SAME LENGTGH" 

SOUTION:df = pd.DataFrame.from_dict(d, orient='index')
df.transpose() 
"""


# In[6]:


df = pd.DataFrame.from_dict(dict_item, orient='index')

df


# In[9]:


new_dataframe=df.transpose()
new_dataframe

