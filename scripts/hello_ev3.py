#!/usr/bin/env python3
from ev3dev.ev3 import *
import os

os.system('setfont Lat15-TerminusBold14')
print('Hello, my name is EV3!')
Sound.speak('Hello, my name is EV3!').wait()

motorLeft = LargeMotor('outD')
motorRight = LargeMotor('outA')

motorLeft.stop_action = 'hold'
motorRight.stop_action = 'hold'
motorLeft.run_to_rel_pos(position_sp = 840, speed_sp = 250)
motorRight.run_to_rel_pos(position_sp = -840, speed_sp = 250)
motorLeft.wait_while('running')
motorRight.wait_while('running')
