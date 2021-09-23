#!/usr/bin/python3

import bluetooth

from ev3dev2.sound import Sound

speaker = Sound()

port = 3
server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_socket.bind(("",port))
server_socket.listen(port)

client_socket,address = server_socket.accept()
print("Accepted connection from", address)

data = client_socket.recv(1024)
while str(data) is not "exit":
    print("Received:", data)
    speaker.speak(str(data))
    data = client_socket.recv(1024)

client_socket.close()
server_socket.close()
