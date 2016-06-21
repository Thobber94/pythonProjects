from BrickPi import *


# Move Forward
def forover():
    BrickPi.MotorSpeed[motor1] = hastighet
    BrickPi.MotorSpeed[motor2] = hastighet


# Move Left
def venstre():
    BrickPi.MotorSpeed[motor1] = hastighet
    BrickPi.MotorSpeed[motor2] = -hastighet


# Move Right
def hoyre():
    BrickPi.MotorSpeed[motor1] = -hastighet
    BrickPi.MotorSpeed[motor2] = hastighet


# Move backward
def revers():
    BrickPi.MotorSpeed[motor1] = -hastighet
    BrickPi.MotorSpeed[motor2] = -hastighet


# Stop
def stop():
    BrickPi.MotorSpeed[motor1] = 0
    BrickPi.MotorSpeed[motor2] = 0


BrickPiSetup()  # setup the serial port for communication

motor1 = PORT_B
motor2 = PORT_C
BrickPi.MotorEnable[motor1] = 1  # Enable the Motor A
BrickPi.MotorEnable[motor2] = 1  # Enable the Motor B
BrickPiSetupSensors()  # Send the properties of sensors to BrickPi
BrickPi.Timeout = 10000  # Set timeout value for the time till which to run the motors after the last command is pressed
BrickPiSetTimeout()  # Set the timeout

hastighet = 125  # Setter hastighet. (Sett en hastighet mellom -255 og 255)
while True:
    inp = str(raw_input())  # Take input from the terminal
    # Move the bot
    if inp == 'w':
        forover()
    elif inp == 'a':
        venstre()
    elif inp == 'd':
        hoyre()
    elif inp == 's':
        revers()
    elif inp == 'x':
        stop()
    BrickPiUpdateValues()  # Update the motor values

    time.sleep(.01)  # sleep for 10 ms
