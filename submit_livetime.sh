#!/bin/sh
#SBATCH --ntasks=1
#SBATCH --mem=10G
#SBATCH --job-name=Rate


export HOME=/atlas/users/mmunozsa/

source  /cvmfs/dampe.cern.ch/centos7/etc/setup.sh
#source ~/astro/bin/activate
dampe_init
export LD_LIBRARY_PATH=/cvmfs/dampe.cern.ch/centos7/opt/DMPSW/latest/lib:${LD_LIBRARY_PATH}


python livetime_calc.py ${1}
