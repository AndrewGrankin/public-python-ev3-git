#!/usr/bin/python3
from ev3dev.ev3 import *
import os

os.system('setfont Lat15-TerminusBold14')
print('Hello, my name is EV3!')
Sound.speak('Hello, my name is EV3!').wait()