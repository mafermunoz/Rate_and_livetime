from root_numpy import root2array
import numpy as np

inF = [x for x in sys.argv if '.root' in x]

for i in inF:
     a=root2array(i)
     time=a['time_s']+a['time_ms']*0.001
     delta_t=time[1:] -time[:-1]
     saa=np.logical_and(a['saa'][1:], a['saa'][:-1])
     time_avg=0.5*(time[1:]+time[:-1])
     =0.5*(a[''][1:]+a[''][:-1])
     lt_wosaa=0
     lt_saa=0
     lt_all=0
    for i,x in enumerate(delta_t):
        if (x<0.1 and x>0.00375 and saa[i]==True):
            lt_wsaa=lt_wsaa+(x-0.00375)
        if (x<0.1 and x>0.00375 and saa[i]==False):
            lt_wosaa=lt_wosaa+(x-0.00375)
        if (x<0.1 and x>0.00375):
            lt_all=lt_all+(x-0.00375)

     np.save("delta_t"+str(i),delta_t)
