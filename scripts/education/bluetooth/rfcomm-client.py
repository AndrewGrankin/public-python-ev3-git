##!/usr/bin/python3

import bluetooth

target_address = None

print("scanning for nearby bluetooth devices...")
print("========================================")
nearby_devices = bluetooth.discover_devices(duration = 10, lookup_names = True)

device_count = len(nearby_devices)
count = 0
devices_dict = dict()

if device_count:
    print("Available devices (" + str(device_count) + "):")
    for device, name in nearby_devices:
        count += 1
        devices_dict[count] = [device, name]
        print(count, name)

    print("=======================================")
    print("type a number of the selected device")
    print("or type 0 to quit")

    choice = int(input())
    if choice != 0 and choice <= device_count:
        print("you've selected", str(devices_dict[choice][1]))
        print("connecting to the device...")
        port = 2
        address = devices_dict[choice][0]
        socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
        socket.connect((address, port))
        socket.send("Hello!")
        socket.close()
    else:
        print("you've typted 0 or a number that is greater than amount of available devices")
