#!/bin/bash
#SBATCH --partition=rhel6-short
#SBATCH --ntasks=1
#SBATCH --mem=60G
#SBATCH --job-name=Rate


export HOME=/atlas/users/mmunozsa/

source /cvmfs/dampe.cern.ch/rhel6-64/etc/setup.sh
source ~/astro/bin/activate
dampe_init > /dev/null

python livetime_calc.py ${1}
