
# coding: utf-8

# # Python Crash Course Exercises 
# 
# This is an optional exercise to test your understanding of Python Basics. The questions tend to have a financial theme to them, but don't look to deeply into these tasks themselves, many of them don't hold any significance and are meaningless. If you find this extremely challenging, then you probably are not ready for the rest of this course yet and don't have enough programming experience to continue. I would suggest you take another course more geared towards complete beginners, such as [Complete Python Bootcamp](https://www.udemy.com/complete-python-bootcamp/)

# ## Exercises
# 
# Answer the questions or complete the tasks outlined in bold below, use the specific method described if applicable.

# ### Task #1
# 
# Given price = 300 , use python to figure out the square root of the price.

# In[3]:

price = 300


# In[6]:

import math as m 
x = m.sqrt(price)
print(x)


# In[6]:




# ### Task #2
# 
# Given the string:
# 
#     stock_index = "SP500"
#    
# Grab '500' from the string using indexing.

# In[7]:

stock_index = "SP500"


# In[9]:

sp500 = stock_index[2:]
print(sp500)


# ### Task #3
# 
# ** Given the variables:**
# 
#     stock_index = "SP500"
#     price = 300
# 
# ** Use .format() to print the following string: **
# 
#     The SP500 is at 300 today.

# In[11]:

stock_index = "SP500"
price = 300


# In[16]:

'The {x} is at {y} today'.format(x = stock_index, y = price )


# ### Task #4
# 
# ** Given the variable of a nested dictionary with nested lists: **
# 
#     stock_info = {'sp500':{'today':300,'yesterday': 250}, 'info':['Time',[24,7,365]]}
#     
# ** Use indexing and key calls to grab the following items:**
# 
# * Yesterday's SP500 price (250)
# * The number 365 nested inside a list nested inside the 'info' key.

# In[18]:

stock_info = {'sp500':{'today':300,'yesterday': 250}, 'info':['Time',[24,7,365]]}


# In[21]:

stock_info['sp500']['yesterday']


# In[23]:

stock_info['info'][1][2]


# ### Task #5
# 
# ** Given strings with this form where the last source value is always separated by two dashes -- **
# 
#     "PRICE:345.324:SOURCE--QUANDL"
#     
# **Create a function called source_finder() that returns the source. For example, the above string passed into the function would return "QUANDL"**

# In[29]:

def source_finder(x): 
    split = x.split('--')[1]
    return split


# In[30]:

source_finder("PRICE:345.324:SOURCE--QUANDL")


# ### Task #5
# 
# ** Create a function called price_finder that returns True if the word 'price' is in a string. Your function should work even if 'Price' is capitalized or next to punctuation ('price!')  **

# In[31]:

def price_finder(x):
    lower = x.lower()
    return 'price' in lower


# In[32]:

price_finder("What is the price?")


# In[33]:

price_finder("DUDE, WHAT IS PRICE!!!")


# In[35]:

price_finder("The is 300")


# ### Task #6
# 
# ** Create a function called count_price() that counts the number of times the word "price" occurs in a string. Account for capitalization and if the word price is next to punctuation. **

# In[84]:

def count_price(x):
    low = x.lower().split()
    count = 0 
    for item in low:
        if 'price' in item:
            count = count+ 1 
    return count 


# In[85]:

s = 'Wow that is a nice price, very nice Price! I said price 3 times.'


# In[86]:

count_price(s)


# ### Task #7
# 
# **Create a function called avg_price that takes in a list of stock price numbers and calculates the average (Sum of the numbers divided by the number of elements in the list). It should return a float. **

# In[87]:

def avg_price(x):
    avg = sum(x)/len(x)
    return avg 


# In[88]:

avg_price([3,4,5])


# # Great job!
