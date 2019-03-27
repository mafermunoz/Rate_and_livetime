from root_numpy import root2array
import numpy as np

inF = [x for x in sys.argv if '.root' in x]

for i in inF:
     a=root2array(i)
     time=a['time_s']+a['time_ms']*0.001
     delta_t=time[1:]-time[:-1]
     saa=np.logical_and(a['saa'][1:], a['saa'][:-1])
     time_avg=0.5*(time[1:]+time[:-1])
     sky_coord=a['sky_coord']
     l=0.5*(sky_coord[3][1:]+sky_coord[3][:-1])
     b=0.5*(sky_coord[4][1:]+sky_coord[4][:-1])
     lt_wosaa=[]
     lt_wosaa_l=[]
     lt_wosaa_b=[]

     lt_saa=[]
     lt_saa_l=[]
     lt_saa_b=[]

     lt_all=[]
     lt_all_l=[]
     lt_all_b=[]
     info=np.stack((delta_t,saa,l,b))
    for i,x in enumerate(delta_t):

        if (x<0.1 and x>0.00375 and saa[i]==True):
            lt_wosaa.append((x-0.00375))
            lt_wosaa_l.append(l[i])
            lt_wosaa_b.append(b[i])


        if (x<0.1 and x>0.00375 and saa[i]==False):
            lt_saa.append((x-0.00375))
            lt_saa_l.append(l[i])
            lt_saa_b.append(b[i])

        if (x<0.1 and x>0.00375):
            lt_all.append((x-0.00375))
            lt_all_l.append(l[i])
            lt_all_b.append(b[i])
     wosaa=np.stack((lt_wosaa,lt_wosaa_l,lt_wosaa_b))
     saa=np.stack((lt_saa,lt_saa_l,lt_saa_b))
     all=np.stack((lt_all,lt_all_l,lt_all_b))

     np.save("Livetime"+str(i),wosaa,saa,all)
