#!/bin/bash
OUTPATH=/beegfs/dampe/users/mmunozsa/timestamp_check/
file_list=/atlas/users/mmunozsa/Rate_and_livetime/list_files_skim

while IFS='' read -r line || [[ -n "$line" ]];
do
    #echo $line
    BSN=$(basename ${line})
    name=${line##*/}
    res=${line%/$name}
    month=${res##*/}
    res=${res%/$month}
    year=${res##*/}
    OUTF=$OUTPATH$year$month$name
    #echo $OUTF
    if [ ! -f ${OUTF} ]; then
			echo $OUTF
			sbatch submit_timestamp_check.sh ${line} ${OUTF} > /dev/null
    fi
done < $file_list
