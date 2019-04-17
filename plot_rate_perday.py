##%matplotlib inline
import matplotlib
import matplotlib.pyplot as plt
##from custom_colors import b as cmap_ds9
import matplotlib.cm as cm
import healpy
import numpy as np
#from astropy.coordinates import SkyCoord  # High-level coordinates
#import astropy.units as u
#import matplotlib.colors as colors
#import math
#import operator
#from astropy.io import fits
matplotlib.rcParams.update({'font.size': 36})
import time
import sys
#from ipywidgets import FloatProgress
#from IPython.display import display
import glob
matplotlib.rcParams['text.usetex'] = True
matplotlib.rcParams['text.latex.unicode'] = True
from lmfit.model import save_modelresult
from lmfit.models import GaussianModel
from astropy.time import Time

file_path='DAMPE_2A_OBS_2016*__rate_info.npy'
txt=glob.glob(file_path)
info=[[] for i in range(len(txt))]
len(info)


print(txt)
for i,file  in enumerate (txt):
    info[i]=np.load(file,encoding='bytes')
    print(info[i].shape)



all_=[[],[]]
saa=[[],[]]
no_saa=[[],[]]
t1=[[],[]]
t2=[[],[]]
t3=[[],[]]
t4=[[],[]]
for i in range (len(info)):
     for j in range(len(info)):
        if(info[i][0][-1]==info[j][0][0]):
            info[i][1][-1]=info[i][1][-1]+info[j][1][0]
            info[j][0]=np.delete(info[j][0],0)
            info[j][1]=np.delete(info[j][1],0)

        if(info[i][2][-1]==info[j][2][0]):
            info[i][3][-1]=info[i][3][-1]+info[j][3][0]
            info[j][2]=np.delete(info[j][2],0)
            info[j][3]=np.delete(info[j][3],0)


        if(info[i][4][-1]==info[j][4][0]):
            info[i][5][-1]=info[i][5][-1]+info[j][5][0]
            info[j][4]=np.delete(info[j][4],0)
            info[j][5]=np.delete(info[j][5],0)

        if(info[i][6][-1]==info[j][6][0]):
            info[i][7][-1]=info[i][7][-1]+info[j][7][0]
            info[j][6]=np.delete(info[j][6],0)
            info[j][7]=np.delete(info[j][7],0)

        if(info[i][8][-1]==info[j][8][0]):
            info[i][9][-1]=info[i][9][-1]+info[j][9][0]
            info[j][8]=np.delete(info[j][8],0)
            info[j][9]=np.delete(info[j][9],0)


        if(info[i][10][-1]==info[j][10][0]):
            info[i][11][-1]=info[i][11][-1]+info[j][11][0]
            info[j][10]=np.delete(info[j][10],0)
            info[j][11]=np.delete(info[j][11],0)

        if(info[i][12][-1]==info[j][12][0]):
            info[i][13][-1]=info[i][13][-1]+info[j][13][0]
            info[j][12]=np.delete(info[j][12],0)
            info[j][13]=np.delete(info[j][13],0)


fig = plt.figure(figsize=(30, 20))
for i in range (len(info)):
    plt.scatter(info[i][0]-1095,info[i][1],color='blue',marker='x',s=100)
    plt.scatter(info[i][2]-1095,info[i][3],color='red',marker='x',s=100)
    plt.scatter(info[i][4]-1095,info[i][5],color='pink',marker='x',s=100)
    plt.scatter(info[i][6]-1095,info[i][7],color='green',marker='x',s=100)
    plt.scatter(info[i][8]-1095,info[i][9],color='cyan',marker='x',s=100)
    plt.scatter(info[i][10]-1095,info[i][11],color='orange',marker='x',s=100)
    plt.scatter(info[i][12]-1095,info[i][13],color='magenta',marker='x',s=100)

plt.yscale('log')
plt.grid(which='Both')
plt.ylabel('\# Events per Day')
plt.xlabel('MET starting from $01.01.2016$')
plt.title("DAMPE Trigger Rate")
plt.savefig('DAMPE_Trigger_RATE_per_day',transparent=True)
