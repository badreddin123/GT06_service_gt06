#!/usr/bin/python

import socket
import binascii

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(("localhost", 8090))
#s.send(binascii.unhexlify('68680f0504035889905831401700df1a00000d0a'))
#s.send("imei:123456789012345,tracker,151030080103,,F,000101.000,A,5443.3834,N,02512.9071,E,0.00,0;")
s.send(binascii.unhexlify('78781101035332702116474470000000720043960d0a78782222120301030b26c900bd52380b8b3b9900140001fe59290e0029dc0000007300f4ce0d0a78782222120301030b35c900bd52310b8b3bbb03145a01fe59290e0029dc000000740051cb0d0a'))

while True:
    print s.recv(1024)

s.close()