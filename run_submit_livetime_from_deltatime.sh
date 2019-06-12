#!/bin/bash

LIST_PATH="/beegfs/dampe/users/mmunozsa/livetime_per_month/DAMPE_2A_OBS_"

for i in {2016..2016}
do
  echo $i
  for j in {2..12}
  do
    if [[ $j -lt 10 ]]; then
        unset SEARCH_PATH
        SEARCH_PATH=$LIST_PATH$i"0"$j
        echo $SEARCH_PATH
        sbatch submit_livetime_from_deltatime.sh $SEARCH_PATH"__deltatime.npz"
    else
        unset SEARCH_PATH
        SEARCH_PATH=$LIST_PATH$i$j
        echo $SEARCH_PATH
        sbatch submit_livetime_from_deltatime.sh  $SEARCH_PATH"__deltatime.npz"
    fi

  done
done
