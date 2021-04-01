# -*- coding: utf-8 -*-
"""
EEG signal extraction
Created on Sat Feb 27 12:16:27 2021
@author: Zhongsheng Peng
"""
# import modules
import cv2
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
sns.set(font_scale=1.2)

#load image
img = cv2.imread('5.tiff',0)
img = cv2.medianBlur(img,5)

#Image binazaion
ret,eeg1 = cv2.threshold(img,127,255,cv2.THRESH_BINARY)
eeg2 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_MEAN_C,\
            cv2.THRESH_BINARY,11,2)
eeg3 = cv2.adaptiveThreshold(img,255,cv2.ADAPTIVE_THRESH_GAUSSIAN_C,\
            cv2.THRESH_BINARY,11,2)

titles = ['Original Image', 'Global Thresholding (v = 127)',
            'Adaptive Mean Thresholding', 'Adaptive Gaussian Thresholding']
images = [img, eeg1, eeg2, eeg3]

for i in range(len(images)):
    plt.subplot(2,2,i+1),plt.imshow(images[i],'gray')
    plt.title(titles[i])
    plt.xticks([]),plt.yticks([])
plt.show()

plt.imshow(eeg1, 'gray')    
plt.show()

#Choose Thresh binary image for converting csv file
pd.DataFrame(eeg1).to_csv("eeg1.csv")

#Below for extracting EEG signals
#load data with numpy 
data = np.genfromtxt('eeg1.csv', delimiter = ',')
#print (data)

# slicing , just keep the array without the first column and first row
# remove paper up and down noise
data1 = data[200:len(data)-200, 1:len(data[0])] 


#replace all 0 to 1 first, 
an_array = np.where(data1 ==0, 1, data1)
#then replace all greater than 1 to 0
an_array1 = np.where(an_array >1, 0, an_array)
#print (an_array1)


#apply sum function to each row
row_sum=np.sum(an_array1,axis=1)
#print(row_mean)


#find the index of a value in the array, list all positions with lines
row_sum1= (np.where(row_sum >0))
#row_sum1= (np.where(row_sum ==0))
#print(row_sum1)

start0=np.zeros(100,dtype=int)
end0=np.zeros(100,dtype=int)

j=0
for i in range(1, len(row_sum) - 1, 1): 
        if (row_sum[i] !=0 and row_sum[i - 1]==0) :     
            start0[j]=i
        if (row_sum[i] !=0 and  row_sum[i + 1]==0):            
            end0[j]=i
            j=j+1



#keep all non zero array to plot
keep0= end0[end0!=0] 
  

a=[]
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
    
  a.append(data2)
  #Transpose row of a to column in b
  b=list(map(list,zip(*a)))  
  np.savetxt("EEG5_all.csv", b, delimiter=",")
  #np.savetxt("EEG5_all.csv", a, delimiter=",")
  np.savetxt("EEG5.csv", data2, delimiter=",")

  
  
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
 









     







    
    
    
    
   











        
        
        
        
        


    
      













