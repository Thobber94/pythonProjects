from BrickPi import *
import curses

BrickPiSetup()

BrickPi.MotorEnable[PORT_B] = 1  # Arm
BrickPi.MotorEnable[PORT_C] = 1  # Grip
BrickPi.MotorEnable[PORT_D] = 1  # Turn
BrickPiSetupSensors()

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)
key = ''

while key != ord('q'):
    key = stdscr.getch()
    BrickPi.MotorSpeed[PORT_D] = 0
    stdscr.refresh()

    if key == curses.KEY_LEFT:
        BrickPi.MotorSpeed[PORT_D] = 50
    elif key == curses.KEY_RIGHT:
        BrickPi.MotorSpeed[PORT_D] = -50
    elif key == curses.KEY_UP:
        BrickPi.MotorSpeed[PORT_B] = 50
    elif key == curses.KEY_DOWN:
        BrickPi.MotorSpeed[PORT_B] = -50

    # Send to the BrickPi
    BrickPiUpdateValues()
    time.sleep(.1)
