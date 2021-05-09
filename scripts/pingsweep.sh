#!/bin/bash

subnet="10.11.1."

for i in {1..254}
do
	ip=$subnet$i
	ping -c 1 $ip | grep "bytes from" & #backgrounding makes run faster
done

