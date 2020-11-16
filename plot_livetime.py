import numpy as np
import sys
import healpy

inF = [x for x in sys.argv if '.npz' in x]
print(inF)

for i in inF:
    d=np.load(i)
    print(i)
    NSIDE=128
    data={'L':d['l'],'B':d['b']}
    pixels=healpy.ang2pix(NSIDE,np.deg2rad(90)-data['B'],(data['L']))

    hitmap = np.zeros(healpy.nside2npix(NSIDE))
    pixels_binned = np.bincount(pixels,weights=d[:,0])
    hitmap[:len(pixels_binned)] =  pixels_binned
    #fig = plt.figure(figsize=(20, 15))
    #healpy.mollview(hitmap,coord=['G'],title='',hold=True)
    #healpy.graticule()
    #fig.savefig('../map_2016_'+str(i))


    outpath="/beegfs/dampe/users/mmunozsa/livetime_per_month/maps/"
    name=i.split("/")[-1].replace('.npz',"_map.npz")
    np.save(outpath+name,hitmap)
