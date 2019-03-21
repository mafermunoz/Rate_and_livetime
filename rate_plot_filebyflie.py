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
days=60/60/24
for i in inF:
    #branches=['time_s','time_ms','saa','trigger','sky_coord','energy','t_coord','c_coord'],selection='saa==1'
     a=root2array(i,branches=['time_s','time_ms'])

     time.append(a['time_s']+a['time_ms']*0.001)
     a=root2array(i,branches=['time_s','time_ms','saa'],selection='saa==1')
     saa.append(a['time_s']+a['time_ms']*0.001)
     a=root2array(i,branches=['time_s','time_ms','saa'],selection='saa==0')
     no_saa.append(a['time_s']+a['time_ms']*0.001)
     a=root2array(i,branches=['time_s','time_ms','saa','trigger'],selection='saa==0 && trigger[0]==1')
     trigger_1.append(a['time_s']+a['time_ms']*0.001)
     a=root2array(i,branches=['time_s','time_ms','saa','trigger'],selection='saa==0 && trigger[1]==1')
     trigger_2.append(a['time_s']+a['time_ms']*0.001)
     a=root2array(i,branches=['time_s','time_ms','saa','trigger'],selection='saa==0 && trigger[2]==1')
     trigger_3.append(a['time_s']+a['time_ms']*0.001)
     a=root2array(i,branches=['time_s','time_ms','saa','trigger'],selection='saa==0 && trigger[3]==1')
     trigger_4.append(a['time_s']+a['time_ms']*0.001)



     time=np.array(time)/60/60/24
     time=time.astype(int)
     print (time)
     saa=np.array(saa)/60/60/24
     saa=saa.astype(int)
     no_saa=np.array(no_saa)/60/60/24
     no_saa=no_saa.astype(int)
     trigger_1=np.array(trigger_1)/60/60/24
     trigger_1=trigger_1.astype(int)
     trigger_2=np.array(trigger_2)/60/60/24
     trigger_2=trigger_2.astype(int)
     trigger_3=np.array(trigger_3)/60/60/24
     trigger_3=trigger_3.astype(int)
     trigger_4=np.array(trigger_4)/60/60/24
     trigger_4=trigger_4.astype(int)

     time_a, time_b=np.unique(time,return_counts=True)
     saa_a, saa_b=np.unique(saa,return_counts=True)
     no_saa_a,no_saa_b=np.unique(no_saa,return_counts=True)
     trigger_1a,trigger_1b=np.unique(trigger_1,return_counts=True)
     trigger_2a,trigger_2b=np.unique(trigger_2,return_counts=True)
     trigger_3a,trigger_3b=np.unique(trigger_3,return_counts=True)
     trigger_4a,trigger_4b=np.unique(trigger_4,return_counts=True)

     print time_a


     info=np.stack((time_a,time_b,saa_a,saa_b,no_saa_a,no_saa_b,trigger_1a,trigger_1b,trigger_2a,trigger_2b,trigger_3a,trigger_3b,trigger_4a,trigger_4b))

     #plt.hist(time,bins=nbins)
     #plt.hist(trigger[:][0],bins=nbins)
     name=i.split("/")[-1].replace("rate.root","_rate_info.npy")
     np.save(name,info)
