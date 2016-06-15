from __future__ import print_function
from BrickPi import *


# Function to clear all the engines (set the speed to 0)
def clearEngines():
    speed = 0
    BrickPi.MotorSpeed[PORT_A] = speed  # N/A
    BrickPi.MotorSpeed[PORT_B] = speed  # Up/Down
    BrickPi.MotorSpeed[PORT_C] = speed  # Rotation
    BrickPi.MotorSpeed[PORT_D] = speed  # Grip


# Function to turn the engine clockwise (rotate the base)
def clockwise(speed):
    clearEngines()
    BrickPi.MotorSpeed[PORT_C] = speed


# Same as over, just counterclockwise
def counterclockwise(speed):
    clearEngines()
    BrickPi.MotorSpeed[PORT_C] = -speed


# Opens the grip
def openarm(speed):
    clearEngines()
    BrickPi.MotorSpeed[PORT_D] = speed


# Closes the grip
def closearm(speed):
    clearEngines()
    BrickPi.MotorSpeed[PORT_D] = -speed


# Raises the arm
def arm_up(speed):
    clearEngines()
    BrickPi.MotorSpeed[PORT_B] = speed


# Lowers the arm
def arm_down(speed):
    clearEngines()
    BrickPi.MotorSpeed[PORT_B] = -speed


# ### initB-C-D are for initializing the arm. Sets everything back to standard position
def initB():
    position = 7
    positionFrom = position - 10
    positionTo = position + 10
    port = PORT_B
    speed = 45

    clearEngines()
    BrickPiUpdateValues()
    while BrickPi.Encoder[port] != position:

        BrickPiUpdateValues()
        if BrickPi.Encoder[port] > position:
            BrickPi.MotorSpeed[port] = -speed
            BrickPiUpdateValues()

        elif BrickPi.Encoder[port] < position:
            BrickPi.MotorSpeed[port] = speed
            BrickPiUpdateValues()

        elif BrickPi.Encoder[port] > positionFrom < positionTo:
            BrickPiUpdateValues()
            BrickPi.MotorSpeed[port] = 0
            BrickPiUpdateValues()
            break

    BrickPiUpdateValues()
    initC()


def initC():
    position = -102
    positionFrom = position - 10
    positionTo = position + 10
    port = PORT_C
    speed = 50

    clearEngines()
    BrickPiUpdateValues()
    while BrickPi.Encoder[port] != position:

        BrickPiUpdateValues()
        if BrickPi.Encoder[port] < position:
            # print(BrickPi.Encoder[port])
            BrickPi.MotorSpeed[port] = speed
            BrickPiUpdateValues()

        elif BrickPi.Encoder[port] > position:
            # print(BrickPi.Encoder[port])
            BrickPi.MotorSpeed[port] = -speed
            BrickPiUpdateValues()

        elif BrickPi.Encoder[port] > positionFrom < positionTo:
            BrickPiUpdateValues()
            BrickPi.MotorSpeed[port] = 0
            BrickPiUpdateValues()
            break

    BrickPiUpdateValues()
    initD()


def initD():
    position = -864
    positionFrom = position - 10
    positionTo = position + 10
    port = PORT_D
    speed = 20

    clearEngines()
    BrickPiUpdateValues()
    while BrickPi.Encoder[port] != position:

        BrickPiUpdateValues()
        # print BrickPi.Encoder[port]
        if BrickPi.Encoder[port] < position:
            BrickPi.MotorSpeed[port] = speed
            BrickPiUpdateValues()

        elif BrickPi.Encoder[port] > position:
            BrickPi.MotorSpeed[port] = -speed
            BrickPiUpdateValues()

        elif BrickPi.Encoder[port] > positionFrom < positionTo:
            BrickPiUpdateValues()
            BrickPi.MotorSpeed[port] = 0
            BrickPiUpdateValues()
            break

    BrickPiUpdateValues()


def values():
    while True:
        clearEngines()
        BrickPiUpdateValues()
        print("Motor B: ")
        print(BrickPi.Encoder[PORT_B])
        print("Motor C: ")
        print(BrickPi.Encoder[PORT_C])
        print("Motor D: ")
        print(BrickPi.Encoder[PORT_D])
        time.sleep(2)


# BrickPiSetup setups all the engines
BrickPiSetup()

# Enables all the engines on PORT_A to PORT_D
BrickPi.MotorEnable[PORT_A] = 1  # Extra
BrickPi.MotorEnable[PORT_B] = 1  # Arm
BrickPi.MotorEnable[PORT_C] = 1  # Grip
BrickPi.MotorEnable[PORT_D] = 1  # Turn
BrickPiSetupSensors()

BrickPi.Timeout = 1000
BrickPiSetTimeout()

print("Starting... Please wait!")
# initB()

# Simple GUI to let the user knows what to press on keyboard
print("\n w: Up "
      "\n s: Down "
      "\n a: Turn clockwise "
      "\n d: Turn counter clockwise "
      "\n x: Open grip "
      "\n c: Close grip "
      "\n -----------------"
      "\n q: Exit")

# Main while loop
while True:

    inp = str(raw_input())

    if inp == "a":
        clockwise(50)
        print("Moving clockwise")
    elif inp == "d":
        counterclockwise(50)
        print("Moving counter clockwise")
    elif inp == "x":
        openarm(25)
        print("Opening grip")
    elif inp == "c":
        closearm(25)
        print("Closing grip")
    elif inp == "w":
        arm_up(50)
        print("Raising arm")
    elif inp == "s":
        arm_down(40)
        print("Lowering arm")
    elif inp == "q":
        sys.exit()
    elif inp == "v":
        values()
    elif inp == "i":
        print("Returning to init position. \n Please wait...")
        initB()
        print("Finished!")
    else:
        clearEngines()
        print("No button")

    # Send to the BrickPi
    BrickPiUpdateValues()
    BrickPiUpdateValues()
    time.sleep(.1)
