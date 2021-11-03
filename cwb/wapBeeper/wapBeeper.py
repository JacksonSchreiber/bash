#!/usr/bin/env python

from scapy.all import Dot11, sniff
import simpleaudio
import sys

wave_obj = simpleaudio.WaveObject.from_wave_file("beep1.wav")
#play_obj = wave_obj.play()
#play_obj.wait_done()

print("WAP Beacon Beeper. Make 802.11 beacon frames audible.")
print("Usage: sudo python3 wapBeeper.py <interface> <target BSSID delimited by colon (:)> <beep frequency (optional, default is a beep per 1 beacon)>")
print("Example: sudo python3 wapBeeper.py wlan0 60:38:E0:B3:5F:41 5")
interface = sys.argv[1]
bssid = sys.argv[2]
beepFreq = 1
if len(sys.argv) > 3:
    beepFreq = sys.argv[3]


def PacketHandler(packet):
    if packet.haslayer(Dot11):
        if packet.type == 0 and packet.subtype == 8: # check if beacon frame
            if packet.addr2 == bssid.lower(): #BSSID of target AP
                global i 
                i = i + 1
                print("Total # of beacons:",i, end='\r')
                if i % int(beepFreq) == 0:
                    play_obj = wave_obj.play()

i = 0
sniff(iface=interface, prn = PacketHandler) #interface name
