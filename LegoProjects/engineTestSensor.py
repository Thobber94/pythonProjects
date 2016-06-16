import re

from BrickPi import *  # import BrickPi.py file to use BrickPi operations

BrickPiSetup()  # setup the serial port for communication

BrickPi.SensorType[PORT_1] = TYPE_SENSOR_EV3_COLOR_M3
BrickPi.MotorEnable[PORT_D] = 1
BrickPiSetupSensors()

while True:
    numbers = []
    result = BrickPiUpdateValues()  # Ask BrickPi to update values for sensors/motors
    if not result:
        color_sensor = BrickPi.Sensor[PORT_1]
        numbers.append(str(color_sensor))

        regex = re.compile('.*L')
        l = numbers
        matches = [string for string in l if not re.match(regex, string)]
        correctList = filter(None, matches)
        if correctList:
            #correctListInt = list(map(int, correctList))
            #print(correctListInt)
            print(correctList)


    time.sleep(.01)
