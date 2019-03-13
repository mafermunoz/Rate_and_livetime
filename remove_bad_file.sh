#!/bin/bash
for f in $(cat badFiles.bad)
do
  rm ${f}
done
