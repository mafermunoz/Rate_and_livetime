count=1
for f in $(cat list_lv2021)
do
    if [ ! -f ${f} ]; then
	echo "File not found: " ${f}
	continue
	fi
    #BSN=$(basename ${f})
    #OUTF=${BSN/".root"/"_energy.root"}

	echo "Submitting: " ${f}

	sbatch submit_livetime.sh ${f} > /dev/null
  #sleep 1
  aa=`squeue -u mmunozsa | wc -l`


    if [ $aa -gt 300 ]; then
      echo "waiting..." $aa
      sleep 20
    fi


done
