#!/bin/sh
#SBATCH --ntasks=1
#SBATCH --mem=10G
#SBATCH --job-name=clone_G


export HOME=/atlas/users/mmunozsa/

source  /cvmfs/dampe.cern.ch/centos7/etc/setup.sh
#source ~/astro/bin/activate
dampe_init
export LD_LIBRARY_PATH=/cvmfs/dampe.cern.ch/centos7/opt/DMPSW/latest/lib:${LD_LIBRARY_PATH}


./rate_new ${1} ${2}
