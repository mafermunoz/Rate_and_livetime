#!/bin/bash

for i in {2015..2019}
do
  echo $i
  for j in {1..12}
  do
    if [[ $j -lt 10 ]]; then
        echo $i"0"$j
    fi
    echo $i$j
  done
done
