import curses

from BrickPi import *

BrickPiSetup()

BrickPi.MotorEnable[PORT_A] = 1
BrickPiSetupSensors()

stdscr = curses.initscr()
curses.cbreak()
stdscr.keypad(1)
key = ''

while key != ord('q'):
    key = stdscr.getch()
    BrickPi.MotorSpeed[PORT_A] = 0
    stdscr.refresh()

    if key == curses.KEY_LEFT:
        BrickPi.MotorSpeed[PORT_A] = 100
    elif key == curses.KEY_RIGHT:
        BrickPi.MotorSpeed[PORT_A] = -100

    # Send to the BrickPi
    BrickPiUpdateValues()
    time.sleep(.1)
