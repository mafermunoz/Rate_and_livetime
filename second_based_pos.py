import numpy as np
import sys

name=sys.argv[1]

a=np.load(name+str("__rate_per_second_pos_sky_nosaa.npy"))#File ending _rate_per_second_pos_sky_nosaa.npy contianing the position information
time=np.load(name+str("__rate_per_second_nosaa.npy"))#File endifit _rate_per_second_nosaa.npy events  per second
print a.shape


unique_values=time[4]
print unique_values.shape
indices_unique_values=time[6]
print indices_unique_values.shape
number_repetitions=time[7]
print number_repetitions.shape

#start_count=time[5]
d_ra=np.array([])
#d_dec=np.array([])
#d_lon=np.array([])
#d_lat=np.array([])
for i in range (len(unique_values)):

    #number_repetitions[i]
    b=np.where(indices_unique_values==i)

    #if (i%1000==0):
    print i
    d_ra=np.append(d_ra,np.average(a[b[0]],axis=0))
    #d_dec=np.append(d_dec,np.average(a[b[0],1]))
    #d_lon=np.append(d_lon,np.average(a[b[0],2]))
    #d_lat=np.append(d_lat,np.average(a[b[0],3]))


#pos=np.vstack((d_ra,d_dec,d_lon,d_lat))

np.save(name+str("averge_pos_per_second"),d_ra)
