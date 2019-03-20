#!/bin/bash
LIST_PATH="/beegfs/dampe/users/mmunozsa/test_rate/DAMPE_2A_OBS_"

for i in {2019}
do
  echo $i
  for j in {1..12}
  do
    if [[ $j -lt 10 ]]; then
        unset SEARCH_PATH
        SEARCH_PATH=$LIST_PATH$i"0"$j"*"
        echo $SEARCH_PATH
        python check_corrupted.py $SEARCH_PATH $i"0"$j
    else
        unset SEARCH_PATH
        SEARCH_PATH=$LIST_PATH$i$j"*"
        echo $SEARCH_PATH
        python check_corrupted.py $SEARCH_PATH $i$j
    fi

  done
done
