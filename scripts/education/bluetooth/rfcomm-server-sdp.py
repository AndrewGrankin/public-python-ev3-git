#!/usr/bin/python3

import bluetooth

#from ev3dev2.sound import Sound

#speaker = Sound()

server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
print("Getting available RFCOMM port...")
#port = bluetooth.get_available_port(bluetooth.RFCOMM)
port = 3
server_socket.bind(("",port))
server_socket.listen(port)
print("Listening on port:", port)

uuid = "ffff"
print("Advertising service EV3...")
bluetooth.advertise_service(server_socket, "EV3 Service", uuid)

client_socket,address = server_socket.accept()
print("Accepted connection from", address)

data = client_socket.recv(1024)
while str(data) != "exit":
    print("Received:", data)
    #speaker.speak(str(data))
    data = client_socket.recv(1024)

client_socket.close()
server_socket.close()
