import numpy as np
import sys
import healpy

inF = [x for x in sys.argv if '__livetime_nosaa.npz' in x]

for i in inF:
    d=np.load(i)
    print(i)
    NSIDE=128
    data={'L':d[:,1],'B':d[:,2]}
    pixels=healpy.ang2pix(NSIDE,np.deg2rad(90)-data['B'],(data['L']))

    hitmap = np.zeros(healpy.nside2npix(NSIDE))
    pixels_binned = np.bincount(pixels,weights=d[:,0])
    hitmap[:len(pixels_binned)] =  pixels_binned
    #fig = plt.figure(figsize=(20, 15))
    #healpy.mollview(hitmap,coord=['G'],title='',hold=True)
    #healpy.graticule()
    #fig.savefig('../map_2016_'+str(i))


    outpath="/beegfs/dampe/users/mmunozsa/livetime_per_month/"
    name=i.split("/")[-1].replace('_livetime_nosaa.npz',"_map_livetime_nosaa.npz")
    np.save(outpath+name,hitmap)
