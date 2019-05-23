/*


  Program  cleaning for searching  photons.
New prgram for cutting photons by variatiing the cuts from program photons_v3_o.cc



new cuts will be added and documeted.

19/01/2017

added out put for the ditribution of the LRMS, TRMS and RRMS, so far no cuts  applied  fot his



*/


//From here there are all the pasted  libraries from Valentina's file
//C libraries
#include <cmath>
#include <iostream>
#include <stdlib.h>
#include <fstream>
#include <sstream>
#include <numeric>
#include <vector>
#include <algorithm>
#include <string>
#include <dirent.h>
#include <sys/types.h>
#include <stdio.h>
#include <sstream>
#include <utility>


//ROOT libraries
#include "TH1F.h"
#include "TFile.h"
#include "TTree.h"
#include "TH2F.h"
#include "TH3F.h"
#include "TString.h"
#include "TGraph.h"
#include "TChain.h"
#include "TF1.h"
#include "TROOT.h"
#include "TSystemDirectory.h"
#include "TSortedList.h"
#include "TStyle.h"
#include "TTree.h"
#include "TH1F.h"
#include <TSystem.h>
#include <TFile.h>
#include "TClonesArray.h"
#include "TTree.h"
#include "TObject.h"
#include "TProfile.h"
#include "TKey.h"
#include "TMath.h"
//DAMPE Libraries
#include "DmpStkLadderAdc.hh"
#include "DmpStkTrack.h"
#include "DmpStkSiCluster.h"
#include "DmpEvtPsdHits.h"
#include "DmpEvtPsdRec.h"
#include "DmpEvtHeader.h"
#include "DmpStkHkeepHeader.h"
#include "DmpEvtBgoHits.h"
#include "DmpEvtBgoRec.h"
#include "DmpEvtNudRaw.h"
#include "DmpHKDSatStatus.h"
#include "DmpEvtSimuHeader.h"
#include "DmpEvtSimuPrimaries.h"
#include "DmpEvtGlobTrack.h"
#include "DmpHKDSatStatus.h"
#include "DmpFilterOrbit.h"
#include "DmpSvcHKDataRead.h"
//Libraries for MC Analysis
#include "DmpEvtMCPrimaryParticle.h"
#include "DmpEvtSimuPrimaries.h"
#include "DmpEvtSimuHeader.h"


using namespace std;


int main(int argc, char** argv){
  //so far this one will need the name of the file only and with the same name _output,  will be our outut file.
  gSystem->Load("libDmpEvent.so");//loading dmp libraries (have the feeling it is redundant)

  //Define constants
  double pi=3.1416;

  //Open file to  analyze
  TFile * file_input= TFile ::Open(argv[1]);
  //Define output text file
    FILE *fevents;
  string output= (string)argv[2];
  string  output1= output + ".txt";
  fevents=fopen(output1.c_str(),"w");
  //Define output  root file


  //Initialization  of the interfac to analyze data.

 const char* filename_svc = argv[2];
  gIOSvc->Set("InData/Read",filename_svc);
  gIOSvc->Set("OutData/NoOutput", "True");
  gIOSvc->Initialize();


  //Get the main collection Tree  and clone it
  TTree* ct=(TTree*)gIOSvc->GetTree("CollectionTree");
  file_output->cd();

  DmpEvtHeader* evtheader = new DmpEvtHeader();
  TBranch *b_evtheader;
  ct->SetBranchAddress("EventHeader",&evtheader,&b_evtheader);


  Long64_t n_entries= ct->GetEntries();
  cout<< n_entries<< endl;

  ct->GetEntry(0); //Get the intial time
  int time_start=evtheader->GetSecond();
  ct->GetEntry(n_entries-1); //Get the final time
  int time_end=evtheader->GetSecond();


  fprintf(fevents,"%d  %d \n",time_start,time_end);





file_output->Write();
file_output->Close();





return 0;

}
