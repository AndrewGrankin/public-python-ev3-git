##!/usr/bin/python3

import sys
import bluetooth

uuid = "ffff"
service_matches = bluetooth.find_service(uuid)

if len(service_matches) == 0:
    print("Couldn't find any service!")
    sys.exit(0)

print(service_matches)
first_match = service_matches[0]
port = first_match["port"]
name = first_match["name"]
host = first_match["host"]

print("Connecting to \"%s\" on %s", name, host)
client_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
client_socket.connect((host, port))

message = str(input())
while message != "exit":
    client_socket.send(message)

client_socket.close()
