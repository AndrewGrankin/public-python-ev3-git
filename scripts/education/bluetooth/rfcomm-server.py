#!/usr/bin/python3

import bluetooth

port = 1
server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_socket.bind(("",port))
server_socket.listen(1)

client_socket,address = server_socket.accept()
print("Accepted connection from", address)

data = client_socket.recv(1024)
print("Received [%s]" %data)

client_socket.close()
server_socket.close()
