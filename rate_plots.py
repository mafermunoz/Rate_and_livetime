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




info=np.stack((time,saa,trigger))
np.save("RATE_info.root",info)
