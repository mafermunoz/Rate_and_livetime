#!/bin/bash

for i in {2015..2019}
do
  print $i
  for j in {1..12}
  do
    print $i$j
  done
done
