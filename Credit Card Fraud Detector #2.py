#!/usr/bin/env python
# coding: utf-8

# In[ ]:


import pandas as pd 
import numpy as np 
import matplotlib.pyplot as plt 
from termcolor import colored as cl 


# In[ ]:


# IMPORTING DATA
import pandas as pd

df = pd.read_csv('Untitled Folder/creditcard.csv')
df.drop('Time', axis = 1, inplace = True)

print(df.head())


# In[ ]:


from termcolor import colored as cl 
cases = len(df)
nonfraud_count = len(df[df.Class == 0])
fraud_count = len(df[df.Class == 1])
fraud_percentage = round(fraud_count/nonfraud_count*100, 2)

print(cl('CASE COUNT', attrs = ['bold']))
print(cl('--------------------------------------------', attrs = ['bold']))
print(cl('Total number of cases are {}'.format(cases), attrs = ['bold']))
print(cl('Number of Valid cases are {}'.format(nonfraud_count), attrs = ['bold']))
print(cl('Number of Fraudulent cases are {}'.format(fraud_count), attrs = ['bold']))
print(cl('Percentage of Fraudulent cases is {}'.format(fraud_percentage), attrs = ['bold']))
print(cl('--------------------------------------------', attrs = ['bold']))


# In[ ]:




