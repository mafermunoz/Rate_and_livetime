#from root_numpy import root2array
import numpy as np
import sys

inF = [x for x in sys.argv if '_deltatime_nosaa.npz' in x]

for i in inF:
    a=np.load(i)
    b=np.stack((a['delta_t'],a['l'],a['b']))
    print (b.shape)
    #time_st01=a[b[:,0]<0.1]
    #time_lt00375=time_st01[time_st01[:,0]>0.00375]
    #time_lt00375[0]=time_lt00375[0]-0.00375


    #outpath="/beegfs/dampe/users/mmunozsa/livetime_per_month/"
    #name=i.split("/")[-1].replace("_deltatime_nosaa.npz","_livetime_nosaa.npz")
    #np.save(outpath+name,a)
