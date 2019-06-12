#from root_numpy import root2array
import numpy as np
import sys

inF = [x for x in sys.argv if '_deltatime_nosaa.npz' in x]

for i in inF:
    a=np.load(i)
    time_st01=a[a['delta_t']<0.1]
    time_lt00375=time_st01[time_st01['delta_t']>0.00375]
    time_lt00375['delta_t']=time_lt00375['delta_t']-0.00375


    outpath="/beegfs/dampe/users/mmunozsa/livetime_per_month/"
    name=i.split("/")[-1].replace("_deltatime_nosaa.npz","_livetime_nosaa.npz")
    np.save(outpath+name,a)
