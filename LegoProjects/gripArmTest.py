from __future__ import print_function
from BrickPi import *

print("Starting... Please wait!")

# BrickPiSetup setups all the engines
BrickPiSetup()

# Enables all the engines on PORT_A to PORT_D
#BrickPi.SensorType[PORT_1] = TYPE_SENSOR_EV3_COLOR_M2
BrickPi.MotorEnable[PORT_A] = 1  # Extra
BrickPi.MotorEnable[PORT_B] = 1  # Arm
BrickPi.MotorEnable[PORT_C] = 1  # Grip
BrickPi.MotorEnable[PORT_D] = 1  # Turn
BrickPiSetupSensors()

BrickPi.Timeout = 1000
BrickPiSetTimeout()

# Global variables
positionArm = 940    # B
positionRotate = -980   # C
positionGrip = 426    # D


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
    print("Moving clockwise")
    BrickPi.MotorSpeed[PORT_C] = speed


# Same as over, just counterclockwise
def counterclockwise(speed):
    clearEngines()
    print("Moving counter clockwise")
    BrickPi.MotorSpeed[PORT_C] = -speed


# Opens the grip
def openarm(speed):
    clearEngines()
    print("Opening grip")
    BrickPi.MotorSpeed[PORT_D] = speed


# Closes the grip
def closearm(speed):
    clearEngines()
    print("Closing grip")
    BrickPi.MotorSpeed[PORT_D] = -speed


# Raises the arm
def arm_up(speed):
    clearEngines()
    print("Raising arm")
    BrickPi.MotorSpeed[PORT_B] = speed


# Lowers the arm
def arm_down(speed):
    clearEngines()
    print("Lowering arm")
    BrickPi.MotorSpeed[PORT_B] = -speed


# ### initB-C-D are for initializing the arm. Sets everything back to standard position
def initB():
    global positionArm
    position = positionArm
    positionFrom = position - 10
    positionTo = position + 10
    port = PORT_B
    speed = 50

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
    global positionRotate
    position = positionRotate
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
    global positionGrip
    position = positionGrip
    positionFrom = position - 10
    positionTo = position + 10
    port = PORT_D
    speed = 10

    clearEngines()
    BrickPiUpdateValues()
    while BrickPi.Encoder[port] != position:

        BrickPiUpdateValues()
        #print(BrickPi.Encoder[port])
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


#def sensor():
#    while True:
#        numbers = []
#        result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors
#        if not result:
#            color_sensor = BrickPi.Sensor[PORT_1]
#            numbers.append(color_sensor)
#            if 1 in numbers:
#                BrickPi.MotorSpeed[PORT_D] = 100
#            else:
#                BrickPi.MotorSpeed[PORT_D] = -100
#
#        time.sleep(.01)


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
    elif inp == "aa":
        clockwise(25)
    elif inp == "d":
        counterclockwise(50)
    elif inp == "dd":
        counterclockwise(25)
    elif inp == "x":
        openarm(25)
    elif inp == "c":
        closearm(25)
    elif inp == "w":
        arm_up(50)
    elif inp == "ww":
        arm_up(35)
    elif inp == "s":
        arm_down(40)
    elif inp == "ss":
        arm_down(20)
    elif inp == "q":
        sys.exit()
    elif inp == "v":
        values()
    elif inp == "i":
        print("Returning to init position. \n Please wait...")
        initB()
        print("Finished!")
    #elif inp == "e":
    #   sensor()
    else:
        clearEngines()
        print("No button")

    # Send to the BrickPi
    BrickPiUpdateValues()
    BrickPiUpdateValues()
    time.sleep(.1)
