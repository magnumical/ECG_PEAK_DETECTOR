'''
### 28,October,2018                                                  
### By : Reza Amini , University of Tabriz                           
###
###
########################################################################
### easiest way to detect peaks of ecg and ploting them             
###
###
########################################################################

'''


import numpy as np
import wfdb
import matplotlib.pyplot as plt
import peakutils
from peakutils.plot import plot as pplot


record=wfdb.rdrecord('100',channels=[0])
fs=record.fs
data=record.p_signal[:,0]



x=input("How much data you need? (exmp=5000 samples) : ")
x=int(x)

indexes = peakutils.indexes(data[:x], thres=0.5, min_dist=0.7)
pplot(np.arange(0, x),data[:x],indexes)


'''
RtoR_samples = indexes[1]-indexes[0]
RtoR_time=RtoR_samples/fs
HR=60/RtoR_time
hr=round(HR,3)
'''

beat=[]
for i in range(len(indexes)):
    RtoR_samples = indexes[i]-indexes[i-1]
    RtoR_time=RtoR_samples/fs
    HR=60/RtoR_time
    beat.append(HR)
hr=round(np.mean(beat),3)

plt.title('Peak Detection\n mean of Heart Rate: '+ str(hr))
plt.show()








