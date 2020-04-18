#!/usr/bin/env python
# coding: utf-8

# In[31]:


#Author:Victor Nkuna
#Created:04/05/2020

import MySQLdb
import pandas as pd
import numpy as np
from matplotlib import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')
import seaborn as sns


# In[2]:


"""A dictionary of list of  values and product description as keys"""
dict_item={"Chips": ["Simba", "Lays"],"Cooldrinks": ["Coke", "Fanta"],"Chocolates": ["Cadbury", "Tex"],"Pies": ["Pepper Steak", "Chicken"],"Fruit": ["Pear", "Apple", "Orange"],"Cupcakes": ["vanilla", "chocolate"],"Veggies":["spinach", "cabbage"]}


# In[4]:


"""Make a dataframe of dictionary of list values"""

DF = pd.DataFrame.from_dict(dict_item,orient='index')


# In[5]:


DF


# In[6]:


"""Transpose invert the original dataframe to make product discripitons(i.e. Names) as columns"""


new_dataframe=DF.transpose()


# In[34]:


"""printing then dataframe """
new_dataframe


# In[29]:


"""converting a  pandas dataframe to a file of csv format"""
csv=new_dataframe.to_csv(r'C:\Users\Administrator\Desktop\sprint2\products.csv',encoding='utf-8',index=True,na_rep='')


# In[30]:


new_dataframe


# In[33]:


"""making visuals from  dataframe products, and their associated brands"""


for i in new_dataframe.columns:
    a=sns.countplot(x=i,data=new_dataframe)
    plt.subplot()
    plt.show()
    
    

