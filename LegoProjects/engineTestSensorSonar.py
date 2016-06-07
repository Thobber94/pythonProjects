from BrickPi import *
import curses, time

BrickPiSetup()

BrickPi.MotorEnable[PORT_A] = 1
#BrickPi.MotorEnable[PORT_B] = 1
#BrickPi.MotorEnable[PORT_C] = 1
#BrickPi.MotorEnable[PORT_D] = 1
BrickPi.SensorType[PORT_2] = TYPE_SENSOR_EV3_INFRARED_M0 
BrickPiSetupSensors()

power = 200

while True:
	#BrickPiUpdateValues()
	#r1 = BrickPi.Sensor[PORT_2]
	#BrickPiUpdateValues()
	#r2 = BrickPi.Sensor[PORT_2]
	#BrickPiUpdateValues()
	#r3 = BrickPi.Sensor[PORT_2]

	BrickPiUpdateValues()
	result = BrickPi.Sensor[PORT_2]

	#if (r1==1 and r2==1 and r3==1 and r1 != 1023 and r2 != 1023 and r3 != 1023):
	#	BrickPi.MotorSpeed[PORT_A] = power
	#	BrickPi.MotorSpeed[PORT_B] = power
 	#	BrickPi.MotorSpeed[PORT_C] = power
	#	BrickPi.MotorSpeed[PORT_D] = power
	#	print(BrickPi.Sensor[PORT_2])
	#	BrickPiUpdateValues()
	#elif (r1 != 1023 and r2 != 1023 and r3 != 1023):
	#	BrickPi.MotorSpeed[PORT_A] = 0
	#	BrickPi.MotorSpeed[PORT_B] = 0
	#	BrickPi.MotorSpeed[PORT_C] = 0
	#	BrickPi.MotorSpeed[PORT_D] = 0
	#	print(BrickPi.Sensor[PORT_2])
	#	BrickPiUpdateValues()
	if (result >= 0 and result <= 255):
		BrickPi.MotorSpeed[PORT_A] = result*5

	else:
		BrickPi.MotorSpeed[PORT_A] = 0
	time.sleep(.1)
