#!/bin/bash
OUTPATH=/beegfs/dampe/users/mmunozsa/test_rate/
count=1
for f in $(cat list_2015_2019)
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
		#sleep 4
		#count=$count+1
		#if [[ $ ]]; then
			#statements
	#	fi
	fi
done
