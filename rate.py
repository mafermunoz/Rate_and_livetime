import ROOT
ROOT.gSystem.Load('libDmpEvent.so')
import sys
import os
import yaml
import glob
import numpy as np

import libDmpEventFilter  as DmpFilter
import libDmpAlgFilterSAATest as FilterTest


def main(inputfile):

    name_file=file_name.split("/")[-1].replace(".root","_")
    myTree=ROOT.DmpChain('CollectionTree')
    myTree.Add(inputfile)
    n_entries=myTree.GetEntries()

    output_path="/beegfs/dampe/users/mmunozsa/rate/"
    pFilter = DmpFilter.DmpFilterOrbit("EventHeader")
    pFilter.ActiveMe()
    sat=

    for i in range (n_entries):
        event=myTree.GetDmpEvent(i)
        sec=event.pEvtHeader().GetSecond()
        ms=event.pEvtHeader().GetMillisecond()
        trigger=np.zeros([4])
        event.pEvtOrbit().
        for j in range (4):
            trigger[j]=event.pEvtHeader().GeneratedTrigger(j)

        saa=pFilter.IsinSAA(sec)
        v1=TVector3(0,0,0)
        #sat=



if __name__ == '__main__':
