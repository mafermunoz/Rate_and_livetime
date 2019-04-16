#!/bin/bash
LIST_PATH="/beegfs/dampe/users/mmunozsa/second_based_info/second_based_infoDAMPE_2A_OBS_"

for i in {2017..2019}
do
  echo $i
  for j in {1..12}
  do
    if [[ $j -lt 10 ]]; then
        unset SEARCH_PATH
        SEARCH_PATH=$LIST_PATH$i"0"$j
        echo $SEARCH_PATH
        sbatch submit_second_based_pos_opt2.sh $SEARCH_PATH
    else
        unset SEARCH_PATH
        SEARCH_PATH=$LIST_PATH$i$j
        echo $SEARCH_PATH
        sbatch submit_second_based_pos_opt2.sh $SEARCH_PATH
    fi

  done
done
