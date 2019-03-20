from root_numpy import root2array
import numpy as np
import sys

inF = [x for x in sys.argv if '.root' in x]

time=[]
trigger=[]
saa=[]

for i in inF:
     a=root2array(i)
     time.append(a['time_s']+a['time_ms']*0.001)
     saa.append(a['saa'])
     trigger.append(a['trigger'])


nbins=(time[-1]-time[0])/60/60/24

#plt.hist(time,bins=nbins)
#plt.hist(trigger[:][0],bins=nbins)
#plt.hist(saa==False,bins=nbins)
#plt.hist(saa=True,bins=nbins)

info=np.stack((time,saa))
np.save("RATE_info.root",info)
