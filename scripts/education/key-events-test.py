#!/usr/bin/python3

import time
import keyboard

while True:
    if keyboard.is_pressed('up'):
        print("up")
    elif keyboard.is_pressed('down'):
        print("down")
    elif keyboard.is_pressed('esc'):
        break
