#!/bin/bash

declare -A aa

i=4

while true; do
  host=$(awk NR==$i RS="\n\n" 'NMAP_all_hosts.txt')
  if [[  $(echo "$host" | wc -l) -gt 5 ]]; then

    ip=$(echo $host | grep -Po '\d+\.\d+\.\d+.\d+')
    
    services=$(echo "$host" | grep -Po '(?<=open\s{2})([\w-]+)$')
    echo "$services" >> services



  elif [[ $(echo "$host" | wc -w ) -eq 0 ]]; then
    break
  fi

  i=$(( $i+1 )) 
done
