#!/bin/bash
#SBATCH --partition=rhel6-long
#SBATCH --ntasks=1
#SBATCH --mem=60G
#SBATCH --job-name=Rate


export HOME=/atlas/users/mmunozsa/

source /cvmfs/dampe.cern.ch/rhel6-64/etc/setup.sh
source ~/astro/bin/activate
dampe_init > /dev/null

python rate_plot_filebyflie.py ${1}
