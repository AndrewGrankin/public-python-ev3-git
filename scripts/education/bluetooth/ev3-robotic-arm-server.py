#!/usr/bin/python3

import time
import bluetooth
from ev3dev2.sound import Sound
from ev3dev2.motor import MediumMotor, OUTPUT_B

# This function is to extract data from the b'data' format
def roboarm_format_name(name):
    prefix_removed = str(name).replace("b\'", "")
    result = prefix_removed.replace("\'", "")
    return result


# Start of the program
speaker = Sound()
mMotor = MediumMotor(OUTPUT_B)

server_socket = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
server_socket.bind(("",bluetooth.PORT_ANY))
server_socket.listen(1)
port = server_socket.getsockname()[1]
print(server_socket.getsockname())
print("Listening on port:", port)

uuid = "11111111-1111-1111-1111-111111111111"
print("Advertising service EV3_Service...")
speaker.speak("Advertising service EV3_Service")
bluetooth.advertise_service(server_socket, "EV3_Service",
                            service_id = uuid,
                            service_classes = [ uuid, bluetooth.SERIAL_PORT_CLASS ],
                            profiles = [ bluetooth.SERIAL_PORT_PROFILE ])

print("Waiting for connection of RFCOMM channel %d" % port)
speaker.speak("Waiting for connection of RFCOMM channel")

client_socket,address = server_socket.accept()
print("Accepted connection from", address)
speaker.speak("Accepted connection from external device")

while True:
    data = client_socket.recv(1024)
    if len(data) == 0:
        break
    data = roboarm_format_name(data)
    print(data)
    if data == "up":
        mMotor.on(speed=50)
    elif data == "down":
        mMotor.on(speed=-50)
    elif data == "idle":
        mMotor.off()
    #speaker.speak(data)
    if data == "esc":
        break

client_socket.close()
server_socket.close()
