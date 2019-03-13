#!/bin/bash
LIST_PATH="/beegfs/dampe/prod/FM/FlightData/2A/"

for i in {2015..2019}
do
  echo $i
  for j in {1..12}
  do
    if [[ $j -lt 10 ]]; then
        echo $i"0"$j
    else
        echo $LIST_PATH$i$j
    fi

  done
done
