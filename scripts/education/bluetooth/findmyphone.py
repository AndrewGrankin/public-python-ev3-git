#!/usr/bin/python3

import bluetooth

target_name = "CAT S31"
target_address = None

print("scanning for nearby bluetooth devices...")
nearby_devices = bluetooth.discover_devices()

print("checking for " + target_name + " device...")  
for device in nearby_devices:
    if bluetooth.lookup_name(device) == target_name:
        target_address = device
        break

if target_address is not None:
    print("found target bluetooth device with address ", target_address)
else:
    print("could not find target bluetooth device nearby")
