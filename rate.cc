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


//#include "histo_def.hpp"
//#include "def_var.hpp"
//#include "eff_cal.hpp"


using namespace std;

int main(int argc, char** argv){
  //so far this one will need the name of the file only and with the same name _output,  will be our outut file.
  gSystem->Load("libDmpEvent.so");//loading dmp libraries (have the feeling it is redundant)
  if (argc!=3){
    printf("The inserted argument is not correct format: ./photons_v6_mc 0(Real Data)/1(MC Data) InputFile OutputFile PDG(MC)");
    return 0;
  }

  //Define constants
  double pi=3.1416;

  //Open file to  analyze
  TFile * file_input= TFile ::Open(argv[1]);
  //Define output  root file
  TFile * file_output;
  file_output= new TFile(argv[2],"RECREATE");

  const char* filename_svc = argv[1];
  gIOSvc->Set("InData/Read",filename_svc);
  gIOSvc->Set("OutData/NoOutput", "True");
  gIOSvc->Initialize();

  DmpFilterOrbit *pFilter =new DmpFilterOrbit("EventHeader");
  pFilter->ActiveMe();
  //Get the main collection Tree  and clone it
  TTree* ct=(TTree*)gIOSvc->GetTree("CollectionTree");
  file_output->cd();




  Int_t time_ms,time_s;
  bool saa;
  Float_t trigger[4];
  Float_t sky_coord[4];
  double t_coord[2];
  double c_coord[2];
  Float_t energy;



  TTree *livetime=new TTree("livetime","TTree with all the required information for livetime and exposure calculations");


  livetime->Branch("time_s",&time_s);
  livetime->Branch("time_ms",&time_ms);
  livetime->Branch("trigger",trigger,"trigger[4]/F");
  livetime->Branch("sky_coord",sky_coord,"sky_coord[4]/F");
  livetime->Branch("t_coord",t_coord,"t_coord[2]/F");
  livetime->Branch("c_coord",c_coord,"c_coord[2]/F");
  livetime->Branch("saa",&saa);
  livetime->Branch("energy",&energy);

  DmpEvtHeader* evtheader = new DmpEvtHeader();
  TBranch *b_evtheader;
  ct->SetBranchAddress("EventHeader",&evtheader,&b_evtheader);


  Long64_t n_entries= ct->GetEntries();
  cout<< n_entries<< endl;

  ct->GetEntry(0); //Get the intial time
  int time_start=evtheader->GetSecond();
  cout<< time_start<< "       "<< time_end<< endl;



  for (int i=0; i< n_entries; i++){

    ct->GetEntry(i);

    time_s=evtheader->GetSecond();
    time_ms=evtheader->GetMillisecond();
    saa=pFilter->IsInSAA( evtheader->GetSecond());
    for (int j=0;j<4;j++){
      trigger[j]=evtheader->GeneratedTrigger(j);

    }

    DmpHKDSatStatus* sat = gHKDataReader->GetSatStatus(evtheader->GetSecond(), evtheader->GetMillisecond());
    Float_t pointcoord[4];
    TVector3 v1(0.0,0.0,1);

    sat->GetParticleCoord(v1,sky_coord);

    sat->GetTRFCoord(t_coord);

    sat->GetCRFCoord(c_coord);

    livetime->Fill();


    }

file_output->Write();
file_output->Close();





return 0;

}
