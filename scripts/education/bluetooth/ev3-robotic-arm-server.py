#!/usr/bin/python3

from bluetooth import *
#from ev3dev2.sound import Sound

#speaker = Sound()

server_socket = BluetoothSocket( RFCOMM )
server_socket.bind(("",PORT_ANY))
server_socket.listen(1)
port = server_socket.getsockname()[1]
print(server_socket.getsockname())
print("Listening on port:", port)

#uuid = "ffff"
uuid = "11111111-1111-1111-1111-111111111111"
#uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"
print("Advertising service EV3_Service...")
advertise_service(server_socket, "EV3_Service",
                  service_id = uuid,
                  service_classes = [ uuid, SERIAL_PORT_CLASS ],
                  profiles = [ SERIAL_PORT_PROFILE ])

print("Waiting for connection of RFCOMM channel %d" % port)

client_socket,address = server_socket.accept()
print("Accepted connection from", address)

while True:
    data = client_socket.recv(1024)
    if len(data) == 0:
        break
    print("Received:", data)
    #speaker.speak(str(data))

client_socket.close()
server_socket.close()
