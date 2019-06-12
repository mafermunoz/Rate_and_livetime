from root_numpy import root2array
import numpy as np
import sys

inF = [x for x in sys.argv if '_deltatime.npz' in x]

for i in inF:

     lt_wosaa=[]
     lt_wosaa_l=[]
     lt_wosaa_b=[]

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
    for j,x in enumerate(delta_t):
         if (x<0.1 and x>0.00375 and saa[j]==False):
             lt_wosaa.append((x-0.00375))
             lt_wosaa_l.append(l[j])
             lt_wosaa_b.append(b[j])


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
     name=i.split("/")[-1].replace("_deltatime.npz","_livetime.npz")
     np.savez(outpath+name,time=lt_wosaa,l=lt_wosaa_l,b=lt_wosaa_b)#,saa,all)
