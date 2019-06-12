#!/bin/bash
LIST_PATH="/beegfs/dampe/users/mmunozsa/test_rate/rate_info_per_month/DAMPE_2A_OBS_"

for i in {2016..2019}
do
  echo $i
  for j in {1..12}
  do
    if [[ $j -lt 10 ]]; then
        unset SEARCH_PATH
        SEARCH_PATH=$LIST_PATH$i"0"$j
        echo $SEARCH_PATH
        sbatch submit_livetime.sh $SEARCH_PATH"_rate.root"
    else
        unset SEARCH_PATH
        SEARCH_PATH=$LIST_PATH$i$j
        echo $SEARCH_PATH
        sbatch submit_livetime.sh $SEARCH_PATH"_rate.root"
    fi

  done
done
