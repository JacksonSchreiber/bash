#!/bin/bash
#set alias with alias vpscon="filepath"

arg=$1

confFile="/home/kali/Desktop/London.conf" #change to wireguard .conf file


if [ $arg = "up" ]
then
	wg-quick up $confFile
	ret=`echo $?`	

	if [ $ret -eq 0 ]
	then
		ssh vps2
	else
		echo "Error in config file"
	fi
elif [ $arg = "down" ]
then
	wg-quick down $confFile	
else
	echo "Command use: ./vpsScript [up/down]"
fi
