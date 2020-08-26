from root_numpy import root2array
import numpy as np
import sys

inF = [x for x in sys.argv if '.root' in x]

for i in inF:
     a=root2array(i,branches=['time_s','time_ms','saa','sky_coord'],selection='saa==0')
     time=a['time_s']+a['time_ms']*0.001
     delta_t=time[1:]-time[:-1]
     #saa=np.logical_and(a['saa'][1:], a['saa'][:-1])
     time_avg=0.5*(time[1:]+time[:-1])
     sky_coord_l=a['sky_coord'][:,2]
     sky_coord_b=a['sky_coord'][:,3]
     l=0.5*(sky_coord_l[1:]+sky_coord_l[:-1])
     b=0.5*(sky_coord_b[1:]+sky_coord_b[:-1])
     livetime=np.zeros(len(delta_t))
     np.subtract(delta_t,0.00375,out=livetime,where=(delta_t>0.00375))
     np.where(delta_t>0.1,livetime*0,livetime)


     #lt_wosaa=[]
     #lt_wosaa_l=[]
     #lt_wosaa_b=[]

     #lt_saa=[]
     #lt_saa_l=[]
     #lt_saa_b=[]

     #lt_all=[]
     #lt_all_l=[]
     #lt_all_b=[]
     #print len(delta_t)
     #print len(l)
     #print len(b)
     #info=np.stack((delta_t,saa,l,b))
    # for j,x in enumerate(delta_t):
    #     if (x<0.1 and x>0.00375 and saa[j]==False):
    #         lt_wosaa.append((x-0.00375))
    #         lt_wosaa_l.append(l[j])
    #         lt_wosaa_b.append(b[j])


         #if (x<0.1 and x>0.00375 and saa[j]==True):
        #     lt_saa.append((x-0.00375))
        #     lt_saa_l.append(l[j])
        #     lt_saa_b.append(b[j])

         #if (x<0.1 and x>0.00375):
        #     lt_all.append((x-0.00375))
        #     lt_all_l.append(l[j])
        #     lt_all_b.append(b[j])
     #wosaa=np.stack((lt_wosaa,lt_wosaa_l,lt_wosaa_b))
     #saa=np.stack((lt_saa,lt_saa_l,lt_saa_b))
     #all=np.stack((lt_all,lt_all_l,lt_all_b))
     outpath="/beegfs/dampe/users/mmunozsa/livetime_per_month/"
     name=i.split("/")[-1].replace("rate.root","_deltatime_nosaa.npz")
     np.savez(outpath+name,delta_t=delta_t,l=l,b=b,time=time_avg,livetime=livetime)#,saa,all)
