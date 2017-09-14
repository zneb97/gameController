import pyautogui
import sys
import time
import arduinoSerial

debounceButton = 0
debounceMove = 0

def translate(value, leftMin, leftMax, rightMin, rightMax):
    # Figure out how 'wide' each range is
    leftSpan = leftMax - leftMin
    rightSpan = rightMax - rightMin
    # Convert the left range into a 0-1 range (float)
    valueScaled = float(value - leftMin) / float(leftSpan)
    # Convert the 0-1 range into a value in the right range.
    return rightMin + (valueScaled * rightSpan)

while True:
    axis = arduinoSerial.getAxis()
    print(axis)
    y = int(axis[1])
    rot = int(axis[3])
    button = int(axis[4])


    #Movement
    #Y
    if(y > 30):
        pyautogui.press('up')
        print('up')
    if(y < -15):
        pyautogui.press('down')
        print('down')

    #Rotation
    if(rot > 220):
        pyautogui.press('left')
        print('left')
    if(rot < 180):
        pyautogui.press('right')
        print('right')


    #Action
    if button == 1:
        pyautogui.press('space')

    time.sleep(.1)
