#!/bin/bash
OUTPATH=/beegfs/dampe/users/mmunozsa/test_rate/
count=1
for f in $(cat list_20201)
do
	if [ ! -f ${f} ]; then
		echo "File not found: " ${f}
		continue
	fi
	BSN=$(basename ${f})
	OUTF=${BSN/".root"/"_rate_new.root"}
	if [ ! -f ${OUTPATH}/${OUTF} ]; then
		echo "Submitting: " ${BSN}
		sbatch submit_rate.sh ${f} ${OUTPATH}/${OUTF} > /dev/null
		aa=`squeue -u mmunozsa | wc -l`


	if [ $aa -gt 300 ]; then
		echo "waiting..." $aa
		sleep 200
		rm slurm-*

	fi

		#count=$count+1
		#if [[ $ ]]; then
			#statements
	#	fi
	fi
done
