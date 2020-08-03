#!/bin/bash
LIST_PATH="/beegfs/dampe/prod/FM/FlightData/2A/"

for i in {2015..2020}
do
  echo $i
  for j in {1..12}
  do
    if [[ $j -lt 10 ]]; then
        unset SEARCH_PATH
        SEARCH_PATH=$LIST_PATH$i"0"$j"*/*/*.root"
        #echo $SEARCH_PATH
        ls $SEARCH_PATH > "List_files"$i"0"$j
    else
        unset SEARCH_PATH
        SEARCH_PATH=$LIST_PATH$i$j"*/*/*.root"
        #echo $SEARCH_PATH
        ls $SEARCH_PATH > "List_files"$i$j
    fi

  done
done
