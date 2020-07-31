#!/bin/bash




aaAdd () {
#$1 = service   $2 = host(ip)
    i=0
    while true; do
        if [ ${aa[$1,$i]} ]; then
            i=$(( $i+1 ))
        else
            aa[$1,$i]=$2
            break
        fi
    done

}

declare -A aa

i=4

while true; do
  host=$(awk NR==$i RS="\n\n" 'NMAP_all_hosts.txt')
  if [[  $(echo "$host" | wc -l) -gt 5 ]]; then

    ip=$(echo $host | grep -Po '\d+\.\d+\.\d+.\d+')
    
    services=$(echo "$host" | grep -Po '(?<=open\s{2})([\w-]+)$')
    
    for x in $services; do
        aaAdd $x $ip
    done


  elif [[ $(echo "$host" | wc -w ) -eq 0 ]]; then
    break
  fi

  i=$(( $i+1 )) 
done

#echo "${!aa[@]}"

for x in ${!aa[@]}; do
    echo "$x" >> output
done
#cat output | sort -d



