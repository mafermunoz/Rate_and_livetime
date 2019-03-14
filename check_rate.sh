#!/bin/bash
OUTPATH=/beegfs/dampe/users/mmunozsa/test_rate/

for f in $(cat List_files201603)
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
    sleep 2
	fi
done
