#!/usr/bin/python
#Uses user list to find users. Prints any verified user

import socket
import sys

if len(sys.argv) != 2:
    print "Usage: vrfy.py <Username List>"
    sys.exit(0)

# Open username list
userList = open(sys.argv[1], "r")

# Create a Socket
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

# Connect to the server
connect = s.connect(('10.11.1.217',25))

#Receive the banner
banner = s.recv(1024)

print banner

# Run VRFY on all usernames in list
for user in userList:
    s.send('VRFY ' + user)
    result = s.recv(1024)
    if "252" in result:
        print result


# Close socket, user list
s.close()
userList.close()
