from root_numpy import root2array
import numpy as np
import sys

inF = [x for x in sys.argv if '.root' in x]

for i in inF:
     a=root2array(i,branches=['time_s','time_ms','trigger'])
     time=a['time_s']+a['time_ms']*0.001
     delta_t=time[1:]-time[:-1]
     #saa=np.logical_and(a['saa'][1:], a['saa'][:-1])
     time_avg=0.5*(time[1:]+time[:-1])


     #np.subtract(delta_t,0.0030725,out=livetime,where=(delta_t>=0.0030725))
     #lv=np.where(delta_t>=1,livetime*0,livetime)

     tt=np.average(time_avg)
     t0=np.sum(trigger[0,:])
     t1=np.sum(trigger[1,:])
     t2=np.sum(trigger[2,:])
     t3=np.sum(trigger[3,:])
     t4=np.sum(trigger[4,:])



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
     outpath="/beegfs/dampe/users/mmunozsa/trigger_rate/"
     name=i.split("/")[-1].replace("rate.root","rate")

     file1 = open(outpath+name+".txt","w+")
     file1.write(str(tt)+"  "+str(t0)+"    "+str(t1)+"  "+str(t2)+" "+str(t3)+" "+str(t4)+"\n")

     file1.close()
