from root_numpy import root2array
import numpy as np
import sys

inF = [x for x in sys.argv if '.root' in x]

# ncounts=[]
# trigger_1=[]
# trigger_2=[]
# trigger_3=[]
# trigger_4=[]
# saa=[]
# no_saa=[]
# time=[]
# days=60/60/24
info=[[] for i in range(14)]
for i in inF:
    #branches=['time_s','time_ms','saa','trigger','sky_coord','energy','t_coord','c_coord'],selection='saa==1'
     #a=root2array(i,branches=['time_s','time_ms'])
     #time=(a['time_s']+a['time_ms']*0.001)
    # a=root2array(i,branches=['time_s','time_ms','saa'],selection='saa==1')
     #saa=(a['time_s']+a['time_ms']*0.001)
     #a=root2array(i,branches=['time_s','time_ms','saa'],selection='saa==0')
     #no_saa=(a['time_s']+a['time_ms']*0.001)
     #a=root2array(i,branches=['time_s','time_ms','saa','trigger'],selection='saa==0 && trigger[0]==1')
     #trigger_1=(a['time_s']+a['time_ms']*0.001)
     #a=root2array(i,branches=['time_s','time_ms','saa','trigger'],selection='saa==0 && trigger[1]==1')
     #trigger_2=(a['time_s']+a['time_ms']*0.001)
     #a=root2array(i,branches=['time_s','time_ms','saa','trigger'],selection='saa==0 && trigger[2]==1')
     #trigger_3=(a['time_s']+a['time_ms']*0.001)
     #a=root2array(i,branches=['time_s','time_ms','saa','trigger'],selection='saa==0 && trigger[3]==1')
     #trigger_4=(a['time_s']+a['time_ms']*0.001)
     a=root2array(i,branches=['time_s','time_ms','saa','trigger','sky_coord'],selection='saa==0')
     pos_sky=(a['sky_coord'])
     no_saa=(a['time_s']+a['time_ms']*0.001)


     #time=time.astype(int)
     #print (time)

     #saa=saa.astype(int)

     no_saa=no_saa.astype(int)

     #trigger_1=trigger_1.astype(int)

     #trigger_2=trigger_2.astype(int)

     #trigger_3=trigger_3.astype(int)

     #trigger_4=trigger_4.astype(int)

     #info[0], info[1],info[2],info[3]=np.unique(time,return_counts=True,return_index=True,return_inverse=True)
     #info[2], info[3]=np.unique(saa,return_counts=True)
     info[4], info[5],info[6],info[7]=np.unique(no_saa,return_counts=True,return_index=True,return_inverse=True)
     #info[6], info[7]=np.unique(trigger_1,return_counts=True)
     #info[8], info[9]=np.unique(trigger_2,return_counts=True)
     #info[10], info[11]=np.unique(trigger_3,return_counts=True)
     #info[12], info[13]=np.unique(trigger_4,return_counts=True)

     #print time_a


     #info=np.stack((time_a,time_b,saa_a,saa_b,no_saa_a,no_saa_b,trigger_1a,trigger_1b,trigger_2a,trigger_2b,trigger_3a,trigger_3b,trigger_4a,trigger_4b))

     #plt.hist(time,bins=nbins)
     #plt.hist(trigger[:][0],bins=nbins)
     outpath="/beegfs/dampe/users/mmunozsa/second_based_info"
     name=i.split("/")[-1].replace("rate.root","_rate_per_second_nosaa.npy")
     name_2=i.split("/")[-1].replace("rate.root","_rate_per_second_pos_sky_nosaa.npy")
     np.save(outpath+name,info)
     np.save(outpath+name_2,pos_sky)
