# coding=utf-8
from BrickPi import *


# Move Forward
def forover():
    BrickPiUpdateValues()
    BrickPi.MotorSpeed[motor1] = -hastighet
    BrickPi.MotorSpeed[motor2] = -hastighet
    BrickPi.MotorSpeed[motor3] = hastighet
    BrickPi.MotorSpeed[motor4] = hastighet
    BrickPiUpdateValues()


# Move Left
def venstre():
    BrickPi.MotorSpeed[motor2] = hastighet
    BrickPi.MotorSpeed[motor3] = -hastighet
    BrickPi.MotorSpeed[motor1] = -hastighet
    BrickPi.MotorSpeed[motor4] = hastighet
    BrickPiUpdateValues()


# Move Right
def hoyre():
    BrickPi.MotorSpeed[motor2] = -hastighet
    BrickPi.MotorSpeed[motor3] = hastighet
    BrickPi.MotorSpeed[motor1] = hastighet
    BrickPi.MotorSpeed[motor4] = -hastighet
    BrickPiUpdateValues()


# Move backward
def revers():
    BrickPi.MotorSpeed[motor1] = hastighet
    BrickPi.MotorSpeed[motor2] = hastighet
    BrickPi.MotorSpeed[motor3] = -hastighet
    BrickPi.MotorSpeed[motor4] = -hastighet
    BrickPiUpdateValues()


# Stop
def stop():
    BrickPi.MotorSpeed[motor1] = 0
    BrickPi.MotorSpeed[motor2] = 0
    BrickPi.MotorSpeed[motor3] = 0
    BrickPi.MotorSpeed[motor4] = 0


BrickPiSetup()  # setup the serial port for communication

motor1 = PORT_B
motor2 = PORT_C
motor3 = PORT_D
motor4 = PORT_A
BrickPi.MotorEnable[motor1] = 1  # Enable the Motor B
BrickPi.MotorEnable[motor2] = 1  # Enable the Motor C
BrickPi.MotorEnable[motor3] = 1  # Enable Motor D
BrickPi.MotorEnable[motor4] = 1  # Enable Motor A
BrickPiSetupSensors()  # Send the properties of sensors to BrickPi
BrickPi.Timeout = 10000  # Set timeout value for the time till which to run the motors after the last command is pressed
BrickPiSetTimeout()  # Set the timeout

hastighet = 255  # Setter hastighet. (Sett en hastighet mellom -255 og 255)

print("Velkommen til Lego BrickPi konkurransen! \n Kontrollene er som følger: \n w + enter: "
      "fremover \n s + enter: revers \n d + enter: høyre \n a + enter: venstre \n x + enter: stopp"
      "\n -------------------------- \n q + enter: avslutt program")

while True:
    inp = str(raw_input())  # Take input from the terminal

    # Move the bot
    if inp.startswith("w"):
        forover()
    elif inp.startswith("a"):
        venstre()
    elif inp.startswith("d"):
        hoyre()
    elif inp.startswith("s"):
        revers()
    elif inp.startswith("x"):
        stop()
    elif inp.startswith("q"):
        sys.exit()
    BrickPiUpdateValues()  # Update the motor values

    time.sleep(.01)  # sleep for 10 ms
