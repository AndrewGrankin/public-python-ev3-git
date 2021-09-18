#!/usr/bin/env python3

from ev3dev2.motor import LargeMotor, OUTPUT_A, OUTPUT_D
from ev3dev2.motor import SpeedDPS, SpeedDPM, SpeedRPS, SpeedRPM
from time import sleep

lMotorLeft = LargeMotor(OUTPUT_D)
lMotorRight = LargeMotor(OUTPUT_A)

# Run motors at some speed (speed is a percantegate of the max motor power)
lMotorLeft.on_for_seconds(speed = 50, seconds = 2) # "speed = 50" - 50% of the max speed of 1050 deg/s for L motor and 1560 for M motor
# or lMotorLeft.on_for_seconds(50, 2)
sleep(0.5)

# Run motors at some speed with use of SpeedDPS/DPM/RPS/RPM funcs.
#  DPS - degrees per second
#  DPM - degress per minute
#  RPS - rotations per second
#  RPM - rotations per minute  
lMotorLeft.on_for_seconds(speed = SpeedDPS(500), seconds = 2)
sleep(0.5)
lMotorLeft.on_for_seconds(speed = SpeedDPM(36000), seconds = 2)
sleep(0.5)
lMotorLeft.on_for_seconds(speed = SpeedRPS(2), seconds = 2)
sleep(0.5)
lMotorLeft.on_for_seconds(speed = SpeedRPM(100), seconds = 2)
sleep(0.5)

# Run motors for certain speed with implicit 'brake' and 'block' paramters (True by default)
# "brake = False" - don't stop the motor after it finishes the command (use friction to stop)
# "block = False" - don't block the run of script (continue to run script)
lMotorLeft.on_for_seconds(speed = SpeedRPS(2), seconds = 3, brake = False, block = False)
lMotorRight.on_for_seconds(speed = SpeedRPS(2), seconds = 3, brake = False, block = True)

#sleep(1)