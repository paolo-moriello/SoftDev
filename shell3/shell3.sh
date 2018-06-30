#!/bin/bash

accessed_files=$(find . ! -path . -type f -atime -30)

for d in $(find . ! -path . -type d | tac)
do
 flag=false
 for e in $accessed_files
 do
  accessed_dir=$(dirname "$e")
  if [[ $accessed_dir == *"$d"* ]]; then
   flag=true;
  fi
 done
 if [ "$flag" = false ]; then tar -zcvf $d.tgz $d; rm -r $d; fi
done
