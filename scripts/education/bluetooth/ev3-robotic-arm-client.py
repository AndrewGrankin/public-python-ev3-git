#!/usr/bin/python3

import sys
import bluetooth
import keyboard
import time


#addr = None
#uuid = "ffff"
#uuid = "94f39d29-7d6d-437d-973b-fba39e49d4ee"

# This function is to extract data from the b'data' format
def roboarm_format_name(name):
    prefix_removed = str(name).replace("b\'", "")
    result = prefix_removed.replace("\'", "")
    return result

# Start of the program
choice = 0
while choice != "exit":
    print("Menu:")
    print("1. To find available services type \"find\".")
    print("2. To exit the program type \"exit\".")
    choice = str(input())
    if choice == "find":
        print("Searching for available bluetooth services...")
        service_matches = []
        try:
            service_matches = bluetooth.find_service()
        except bluetooth.btcommon.BluetoothError as btError:
            print("This is bluetooth error")
            print(btError)
        except:
            print("Some error:", sys.exc_info())
        service_count = len(service_matches)
        if service_count == 0:
            print("Couldn't find any service!")
        else:
            print("*** Available services ***")
            count = 0
            for service in service_matches:
                print("Service:", count, "name:", roboarm_format_name(service["name"]))
                count += 1
            print("**************************")

            print("Type the number of the service you want to connect to:")
            service_number = int(input())
            if service_number < 0 or service_number > service_count - 1:
                print("Wrong service number!")
                continue
            else:
                current_match = service_matches[service_number]
                port = current_match["port"]
                name = current_match["name"]
                host = current_match["host"]

                print("Connecting to", roboarm_format_name(name), "on host", host, "and port", port)
                client_socket = bluetooth.BluetoothSocket( bluetooth.RFCOMM )
                try:
                    client_socket.connect((host, port))
                except:
                    print("Some error:", sys.exc_info())
                    continue

                while True:
                    #print("Enter some message:")
                    message = "idle"
                    if keyboard.is_pressed('up'):
                        message = "up"
                    if keyboard.is_pressed('down'):
                        message = "down"
                    if keyboard.is_pressed('esc'):
                        message = "esc"
                    client_socket.send(message)
                    if message == "esc":
                        break
                    time.sleep(0.5)

                client_socket.close()
        
    else:
        choice = "exit"
        print("Good bye!")
