
# coding: utf-8

# # Pandas Exercises

# Time to test your new pandas skills! Use the two csv files in this folder to complete the tasks in bold below!
# 
# ** NOTE: ALL TASKS MUST BE DONE IN ONE LINE OF PANDAS CODE. GOT STUCK? NO PROBLEM! CHECK OUT THE SOLUTIONS LECTURE! **

# ** Import pandas and read in the banklist.csv file into a dataframe called banks. **

# In[1]:

import pandas as pd 
import numpy as np 

banks = pd.read_csv('banklist.csv')


# In[2]:

banks.head()


# ** Show the head of the dataframe **

# In[26]:

# CODE HERE


# In[37]:




# ** What are the column names? **

# In[3]:

# CODE HERE 

banks.columns


# In[29]:




# ** How many States (ST) are represented in this data set? **

# In[5]:

banks['ST'].nunique()


# In[33]:




# ** Get a list or array of all the states in the data set. **

# In[9]:

# CODE HERE

banks['ST'].unique()


# In[32]:




# ** What are the top 5 states with the most failed banks? **

# In[91]:

# CODE HERE
banks['ST'].value_counts().head(5)

banks.groupby("ST").count().sort_values('Bank Name',ascending=False).iloc[:5]


# In[35]:




# ** What are the top 5 acquiring institutions? **

# In[16]:

# CODE HERE

banks['Acquiring Institution'].value_counts().head(5)


# In[14]:




# ** How many banks has the State Bank of Texas acquired? How many of them were actually in Texas?**

# In[28]:

# CODE HERE
State_Acq = banks[banks['Acquiring Institution'] == 'State Bank of Texas' ]
State_in_TX = banks[(banks['Acquiring Institution'] == 'State Bank of Texas') & (banks['ST'] == 'TX') ]


# In[31]:

State_in_TX.head()


# In[30]:

State_Acq.head()


# In[15]:




# ** What is the most common city in California for a bank to fail in?**

# In[ ]:

# CODE HERE

banks[banks['ST']=='CA'].groupby('City').count().sort_values('Bank Name',ascending=False).head(1)


# In[51]:

CA = banks[banks['ST'] == 'CA']
CA['City'].value_counts()
City = CA[CA['City'] =='Los Angeles']


# In[24]:




# ** How many failed banks don't have the word "Bank" in their name? **

# In[89]:

# banks['Bank Name'].apply(lambda name: 'Bank' not in name).value_counts()
sum(banks['Bank Name'].apply(lambda name: 'Bank' not in name))
   


# In[ ]:




# In[55]:




# ** How many bank names start with the letter 's' ? **

# In[ ]:

# CODE HERE

sum(banks['Bank Name'].apply(lambda name:name[0].upper() =='S'))


# In[58]:




# ** How many CERT values are above 20000 ? **

# In[61]:

# CODE HERE
Cert_20k = banks[banks['CERT']>= 20000]

Cert_20k['CERT'].count()


# In[64]:




# ** How many bank names consist of just two words? (e.g. "First Bank" , "Bank Georgia" )**

# In[90]:

# CODE HERE
sum(banks['Bank Name'].apply(lambda name: len(name.split())==2))


# In[67]:




# **Bonus: How many banks closed in the year 2008? (this is hard because we technically haven't learned about time series with pandas yet! Feel free to skip this one!**

# In[ ]:

# CODE HERE

# WE WILL LEARN A MUCH BETTER WAY TO DO THIS SOON!
sum(banks['Closing Date'].apply(lambda date: date[-2:]) == '08')

# Better way
# sum(pd.to_datetime(banks['Closing Date']).apply(lambda date: date.year) == 2008)


# In[54]:





# # GREAT JOB!
