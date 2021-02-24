#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#BIOT670 Spring2021


# In[ ]:


# Author: Yekaterina Unnikumaran


# In[ ]:


# Extracting Features Using Pixels in txt files from conversion

# First step is put eeg1.txt file in our path so we can read it and work with it, in Notebooks I can simply use read code
# as it is already in my environment since I am using Anaconda


# In[2]:


import pandas as pd
eeg1 = pd.read_table('eeg1.txt')
eeg1.head()


# In[ ]:


# Source for code above: https://www.youtube.com/watch?v=edjBYUj_5e0

#This puts my pixels in a table, but I still need to clean it up


# In[ ]:


# The code below drops all the rows that contain missing values, 'dropna' removes rows that contain missing data for even
# just one column


# In[5]:


eeg1 = eeg1.dropna()


# In[7]:


eeg1.dropna()


# In[ ]:


# Source for code above: https://datacarpentry.org/python-ecology-lesson/04-data-types-and-format/index.html

#The table above now only contains the area in which a value is found

