import Tkinter
from BrickPi import *


# Global variables


def clearEngines():
    speed = 0
    BrickPi.MotorSpeed[PORT_A] = speed  # N/A
    BrickPi.MotorSpeed[PORT_B] = speed  # Up/Down
    BrickPi.MotorSpeed[PORT_C] = speed  # Grip
    BrickPi.MotorSpeed[PORT_D] = speed  # Rotation


def clockwise(speed):
    clearEngines()
    BrickPi.MotorSpeed[PORT_D] = speed


def counterclockwise(speed):
    clearEngines()
    BrickPi.MotorSpeed[PORT_D] = -speed


def openarm(speed):
    clearEngines()
    BrickPi.MotorSpeed[PORT_C] = speed


def closearm(speed):
    clearEngines()
    BrickPi.MotorSpeed[PORT_C] = -speed


def arm_up(speed):
    clearEngines()
    BrickPi.MotorSpeed[PORT_B] = speed


def arm_down(speed):
    clearEngines()
    BrickPi.MotorSpeed[PORT_B] = -speed


BrickPiSetup()

BrickPi.MotorEnable[PORT_B] = 1  # Arm
BrickPi.MotorEnable[PORT_C] = 1  # Grip
BrickPi.MotorEnable[PORT_D] = 1  # Turn
BrickPiSetupSensors()

BrickPi.Timeout = 1000
BrickPiSetTimeout()

while True:
    inp = str(raw_input())

    if inp == "a":
        clockwise(50)
        print "Moving clockwise"
    elif inp == "d":
        counterclockwise(50)
        print "Moving counter clockwise"
    elif inp == "x":
        openarm(25)
        print "Opening grip"
    elif inp == "c":
        closearm(25)
        print "Closing grip"
    elif inp == "w":
        arm_up(50)
        print "Raising arm"
    elif inp == "s":
        arm_down(30)
        print "Lowering arm"
    else:
        clearEngines()
        print "No button"

    # Send to the BrickPi
    BrickPiUpdateValues()
    BrickPiUpdateValues()
    time.sleep(.1)
