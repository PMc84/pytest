#!/bin/bash

for file in ./testfile/file.*; do
  increment=$(echo $file | cut -d. -f3-)
  increment=$(( 10#$increment +1 ))
  printf -v increment "%03d" $increment
  echo "$file" "${file//[0-9]}$increment";
done
