#from root_numpy import root2array
import numpy as np
import sys

inF = [x for x in sys.argv if '_deltatime_nosaa.npz' in x]

for i in inF:
    a=np.load(i)
    b=np.stack((a['delta_t'],a['l'],a['b']),axis=1)
    del a
    print (b.shape)
    time_st01=b[b[:,0]<0.1]
    del b

    time_lt00375=time_st01[time_st01[:,0]>0.003075]
    del time_st01
    time_lt00375[0]=time_lt00375[0]-0.003075##0.003075
    print(time_lt00375.shape)

    outpath="/beegfs/dampe/users/mmunozsa/livetime_per_month/"
    name=i.split("/")[-1].replace("_deltatime_nosaa.npz","_livetime_nosaa2.npz")
    np.save(outpath+name,time_lt00375)
    del time_lt00375
