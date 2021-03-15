#!/usr/bin/env python
# coding: utf-8

# In[1]:


#BIOT670 Spring 2021
#EEG Project: Signal Extraction
#Date Created: Mar 4, 2021
#Author: Yekaterina Unnikumaran


# In[2]:


# import modules
import time as time
import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale=1.2)
from sklearn.feature_extraction import image
from sklearn.feature_extraction.image import grid_to_graph
from sklearn.cluster import AgglomerativeClustering
from sklearn.utils.fixes import parse_version
from scipy.ndimage.filters import gaussian_filter
import skimage
import pytiff #fairly new package, uploaded tiff file and automatically converted it to an array


# In[3]:


with pytiff.Tiff("5.tiff") as handle:
        part = handle[100:200, 200:400] #supports tiled tiffs and bigtiff, so you can read parts of large images


# In[4]:


part #prints out image as array


# In[7]:


#slicing to keep ony array w/o first column and first row
#remove paper noise
eeg1 = part[200:len(part)-200, 1:len(part[0])]


# In[9]:


#replace all 0 to 1 first, 
an_array = np.where(eeg1 ==0, 1, eeg1)
#then replace all greater than 1 to 0
an_array1 = np.where(an_array >1, 0, an_array)
#print (an_array1)


# In[10]:


#apply sum function to each row
row_sum=np.sum(an_array1,axis=1)
#print(row_mean)


# In[11]:


#find the index of a value in the array, list all positions with lines
row_sum1= (np.where(row_sum >0))
#row_sum1= (np.where(row_sum ==0))
#print(row_sum1)


# In[12]:


start0=np.zeros(100,dtype=int)
end0=np.zeros(100,dtype=int)


# In[13]:


j=0
for i in range(1, len(row_sum) - 1, 1): 
        if (row_sum[i] !=0 and row_sum[i - 1]==0) :     
            start0[j]=i
        if (row_sum[i] !=0 and  row_sum[i + 1]==0):            
            end0[j]=i
            j=j+1


# In[14]:


#keep all non zero array to plot
keep0= end0[end0!=0]


# In[15]:


#use loop for generating figures   
for k in range(len(keep0)):   
    
  part1 = an_array1[start0[k]:end0[k],0:len(data[0])]
  part1=part1.astype('int8')
  m1 = np.arange(len(part1),0,-1)

  try1 = np.zeros([len(part1),len(data1[0])],dtype=int)
  for i in range(len(part1)):
      try0=m1[i]
      for j in range(len(data1[0])):
          if part1[i,j]==1:
              try1[i,j]=m1[i]
            
#calculated an unique number for each column

  try2 = np.sum(try1,axis=0)/np.sum(np.array(try1) >0,axis=0)
  #adjusted the line to zero as middle 
  data2= np.where(try2>0,try2-len(part1)/2, try2)
    
# Define sampling frequency and time vector
  sf = 100.
  time = np.arange(data2.size) / sf

# Plot the signal
  fig, ax = plt.subplots(1, 1, figsize=(12, 4))
  plt.plot(time, data2, lw=1.5, color='k')
  plt.xlabel('Time (seconds)')
  plt.ylabel('Voltage')
  plt.xlim([time.min(), time.max()])
  plt.title('EEG signal')
  sns.despine()


# In[16]:


sns.despine()


# In[ ]:




