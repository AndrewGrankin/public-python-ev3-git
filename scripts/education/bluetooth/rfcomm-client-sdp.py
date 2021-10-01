##!/usr/bin/python3

import sys
from bluetooth import *


addr = None
uuid = "ffff"
#uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
service_matches = find_service( uuid = uuid, address = addr )

if len(service_matches) == 0:
    print("Couldn't find any service!")
    sys.exit(0)

print("********************")
for key, value in service_matches[0].items():
    print(key, value)
print("********************")

first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("Connecting to", name, "on host", host, "and port", port)
client_socket = BluetoothSocket( RFCOMM )
client_socket.connect((host, port))

while True:
    print("Enter some message:")
    message = str(input())
    client_socket.send(message)
    if message == "exit":
        break

client_socket.close()
