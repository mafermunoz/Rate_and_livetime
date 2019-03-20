from root_numpy import root2array
import numpy as np
import sys

inF = [x for x in sys.argv if '.root' in x]

ncounts=[]
trigger_1=[]
trigger_2=[]
trigger_3=[]
trigger_4=[]
saa=[]
no_saa=[]
time=[]

for i in inF:
     a=root2array(i)
     time.append(a['time_s']+a['time_ms']*0.001)
     a=root2array(i,selection='saa=True')
     saa.append(a['time_s']+a['time_ms']*0.001)
     a=root2array(i,selection='saa=False')
     no_saa.append(a['time_s']+a['time_ms']*0.001)


nbins=(time[-1]-time[0])/60/60/24

#plt.hist(time,bins=nbins)
#plt.hist(trigger[:][0],bins=nbins)
#plt.hist(saa==False,bins=nbins)
#plt.hist(saa=True,bins=nbins)

info=np.stack((time,saa))
np.save("RATE_info.root",info)
