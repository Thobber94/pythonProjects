from BrickPi import *


def clearEngines():
    speed = 0
    BrickPi.MotorSpeed[PORT_A] = speed  # N/A
    BrickPi.MotorSpeed[PORT_B] = speed  # Up/Down
    BrickPi.MotorSpeed[PORT_C] = speed  # Grip
    BrickPi.MotorSpeed[PORT_D] = speed  # Rotation


BrickPiSetup()

BrickPi.MotorEnable[PORT_A] = 1
BrickPiSetupSensors()

BrickPi.Timeout = 1000
BrickPiSetTimeout()
BrickPiUpdateValues()

print "\n w: Up " \
      "\n s: Down " \
      "\n a: Turn clockwise " \
      "\n d: Turn counter clockwise " \
      "\n x: Open grip " \
      "\n c: Close grip " \
      "\n -----------------" \
      "\n q: Exit"

while True:
    inp = str(raw_input())

    if inp == "180":
        motorRotateDegree([50], [180], [PORT_A])
    elif inp == "360":
        motorRotateDegree([50], [360], [PORT_A])
    elif inp == "x":
        while BrickPi.Encoder[PORT_A] % 720 / 2 != 250:
            BrickPi.MotorSpeed[PORT_A] = 30
            print (BrickPi.Encoder[PORT_A] % 720 / 2)
            BrickPiUpdateValues()


    # Send to the BrickPi
    BrickPiUpdateValues()
    BrickPiUpdateValues()
    time.sleep(.1)
