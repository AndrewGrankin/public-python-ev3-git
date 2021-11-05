#!/usr/bin/env python3

from time import sleep
from ev3dev2.motor import MediumMotor, LargeMotor
from ev3dev2.motor import OUTPUT_A, OUTPUT_B, OUTPUT_C, OUTPUT_D
from ev3dev2.motor import SpeedDPS, SpeedPercent, MoveTank
from ev3dev2.sensor import INPUT_1, INPUT_2, INPUT_3, INPUT_4
from ev3dev2.sensor.lego import TouchSensor, InfraredSensor
from ev3dev2.led import Leds
from ev3dev2.sound import Sound

SPEAKER = Sound()
INFRARED_SENSOR = InfraredSensor(INPUT_4)
BASE_M_MOTOR = MediumMotor(OUTPUT_D)
FIRST_SECTION_L_MOTOR = LargeMotor(OUTPUT_A)
SECOND_SECTION_L_MOTOR = LargeMotor(OUTPUT_B)

SPEAKER.speak("I am ready")

while True:
    if INFRARED_SENSOR.top_left():
        BASE_M_MOTOR.on(speed = SpeedDPS(-120), brake = True, block = False)
    elif INFRARED_SENSOR.bottom_left():
        BASE_M_MOTOR.on(speed = SpeedDPS(120), brake = True, block = False)
    elif INFRARED_SENSOR.top_right():
        FIRST_SECTION_L_MOTOR.on(speed = SpeedDPS(-120), brake = True, block = False)
    elif INFRARED_SENSOR.bottom_right():
        FIRST_SECTION_L_MOTOR.on(speed = SpeedDPS(120), brake = True, block = False)
    else:
        BASE_M_MOTOR.off()
        FIRST_SECTION_L_MOTOR.off()

# TODO: Add code here
