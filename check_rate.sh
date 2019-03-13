#!/bin/bash
OUTPATH=/beegfs/dampe/users/mmunozsa/test_rate/

for f in $(cat inFiles.txt)
do
	if [ ! -f ${f} ]; then
		echo "File not found: " ${f}
		continue
	fi
	BSN=$(basename ${f})
	OUTF=${BSN/".root"/"_rate.root"}
	if [ ! -f ${OUTPATH}/${OUTF} ]; then
		echo "Submitting: " ${BSN}
		sbatch submit_rate.sh ${f} ${OUTPATH}/${OUTF} > /dev/null
	fi
done
