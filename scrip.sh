#!/bin/bash

declare -A aa #declare associative array (hash table)

i=4 # start on line 4

while true; do
  host=$(awk NR==$i RS="\n\n" "$1") #split up by individual host 
  if [[  $(echo "$host" | wc -l) -gt 5 ]]; then #ignore hosts with less than 5 lines of info

    ip=$(echo $host | grep -Po '\d+\.\d+\.\d+.\d+') #filter ip
    
    services=$(echo "$host" | grep -Po '(?<=open\s{2})([\w-]+)$') #filter service
    
    for x in $services; do #add all host's services as keys, set host's IP as their value
      aa[$x]+="$ip
"
    done


  elif [[ $(echo "$host" | wc -w ) -eq 0 ]]; then #at end of file, break loop
    break
  fi

  i=$(( $i+1 )) 
done


for x in ${!aa[@]}; do #display services and their associated hosts. only unique hosts
  echo "Service: $x Count: $(( $(echo "${aa[$x]}" | uniq | wc -l) - 1 ))
=======================================" #get count of IPs per service
  echo "${aa[$x]}" | uniq
done








