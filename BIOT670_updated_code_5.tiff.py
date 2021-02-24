#!/usr/bin/env python
# coding: utf-8

# In[ ]:


#BIOT670 Spring 2021 Capstone


# In[ ]:


#Author:Zhonsheng Peng, Editor: Yekaterina Unnikumaran


# In[39]:


import cv2


# In[40]:


import pandas as pd


# In[59]:


from matplotlib import pyplot as plt


# In[60]:


#added following line, to align to GUI at some point


# In[61]:


get_ipython().run_line_magic('matplotlib', 'inline')


# In[45]:


img = cv2.imread('5.tiff',0)


# In[46]:


img = cv2.medianBlur(img,5)


# In[ ]:


#changed eeg to eeg1 to align with code further down in script


# In[47]:


ret, eeg1 = cv2.threshold(img, 127, 255, cv2.THRESH_BINARY)


# In[48]:


eeg2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,                             cv2.THRESH_BINARY,11,2)


# In[49]:


eeg3 = cv2.adaptiveThreshold(img, 255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,                            cv2.THRESH_BINARY, 11,2)


# In[50]:


titles = ['Original Image', 'Global Thresholding(v = 127)', 
          'Adaptive Mean Thresholding','Adaptive Gaussian Thresholding']


# In[51]:


images = [img, eeg1, eeg2, eeg3]


# In[ ]:


#In code below, for plt.show(), changed eeg1 to eeg1.all, I kept getting an error when running this last part of the script


# In[57]:


for i in range(len(images)):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]), plt.yticks([])
    plt.show(eeg1.all, "gray")
    pd.DataFrame(eeg1).to_csv("eeg1.txt")


# In[ ]:




