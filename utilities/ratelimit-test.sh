#!/bin/sh

for i in `cat links.txt`;
do
  echo $i
  curl --header "Content-Type: application/json" -X POST localhost:5000/encode --data '{"url": "'$i'"}'
  sleep 1
done
