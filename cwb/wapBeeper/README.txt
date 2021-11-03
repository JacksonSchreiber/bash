Install instructions:
1.) Download scapy with pip
2.) Get these dependencies for the beeping sound
sudo apt-get install -y python3-dev libasound2-dev
3.) download simpleaudio with pip (be sure install with sudo)
sudo pip install simpleaudio
4.) Run the program with sudo


Monitor mode instructions:
1.) sudo ifconfig wlan0 down #shutdown int
2.) sudo airmon-ng check kill #shutdown network manager..
Restore with:
	service network-manager restart
	service NetworkManager restart
	service avahi-daemon restart


3.) sudo iwconfig wlan0 mode monitor
4.) sudo iwconfig wlan0 channel <channel number of target> #sets a fixed channel rather than channel hopping
5.) sudo ifconfig wlan0 up
6.) iw dev #check channel number. run a few times, make sure it doesn't change
