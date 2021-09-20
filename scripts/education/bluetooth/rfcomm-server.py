#!/usr/bin/python3

import bluetooth

port = 1
server_socket = bluetooth.BluetoothSocket(bluetooth.RFCOMM)
server_socket.bind(("",port))
server_socket.listen(1)
