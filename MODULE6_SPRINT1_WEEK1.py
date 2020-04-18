#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#Author:Victor Nkuna
#Created: 30/ March/2020


# In[15]:


#Author:Victor Nkuna
#Created: 30/ March/2020
1
import pandas as pd
2
import numpy as np
3
from matplotlib  import pyplot as plt
get_ipython().run_line_magic('matplotlib', 'inline')

"""Creating a dictionary list of products and their associated name"""


d={"Chips":pd.Series(["Simba","Lays"]),"Cooldrinks":pd.Series(["Coke","Fanta"]),"Chocolates":pd.Series(["Cadbury","Tex"]),"Pies":pd.Series(["Pepper Steak","Chicken"]),"Fruit":pd.Series(["Pear","Apple","Orange"]),"Cupcakes":pd.Series(["vanilla","chocolate"]),"Veggies":pd.Series(["spinach","cabbage"])}

df=pd.DataFrame(d)


print(df)






# In[13]:


df.head()


# In[3]:



"""The are three rows=[0,1,2](datapoints) and column=["CHIPS",CHOCOLATES,..etc]"""
np.shape(df)


# In[5]:


"""describe the products of the vault
in the datafraem(i.e. table named=df)
 The count shows number of different products(num) and unique shows if they homogenous(same)
 
 or otherwise unique=different
"""


df.describe()


# In[7]:


"""Filter vault items by the following products:1.Chips,
                                                2.Cooldrinks
                                                3.Chocolates
"""
filter_product=df.filter(["Chips","Cooldrinks","Chocolates"])

filter_product


# In[ ]:





# In[ ]:




