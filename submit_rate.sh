#!/bin/bash
#SBATCH --partition=rhel6-veryshort
#SBATCH --ntasks=1
#SBATCH --mem=10G
#SBATCH --job-name=ntSelec


export HOME=/atlas/users/mmunozsa/

source /cvmfs/dampe.cern.ch/rhel6-64/etc/setup.sh
dampe_init > /dev/null

./rate ${1} ${2}
