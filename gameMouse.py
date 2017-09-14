import pyautogui
import sys
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
    x = int(axis[0])
    y = int(axis[1])
    button = int(axis[4])

    #Make coordinates fair
    #X
    xFlag = 0
    if x>10:
        moveXpos = translate(x, 10, 80, 1, 40)
        moveXneg = 0
    elif x<-30:
        moveXneg = translate(x, -145, -30, -40, -1)
        moveXpos = 0
    else:
        moveXpos = 0
        moveXneg = 0
        xFlag = 1
    #Y
    yFlag = 0
    if y>30:
        moveYpos = translate(y, 30, 192, -1, -40)
        moveYneg = 0
    elif y<-15:
        moveYneg = translate(y, -126, -30, 40, 1)
        moveYpos = 0
    else:
        moveYpos = 0
        moveYneg = 0
        yFlag = 1


    #Get larger of two values
    #X
    if(debounceMove == 0):
        if(abs(moveXpos) > abs(moveXneg)):
            moveX = abs(moveXpos)
            dirX = 1
        elif(abs(moveXpos) < abs(moveXneg)):
            moveX = abs(moveXneg)
            dirX = -1
        #Y
        if(abs(moveYpos) > abs(moveYneg)):
            moveY = abs(moveYpos)
            dirY = 1
        elif(abs(moveYpos) < abs(moveYneg)):
            moveY = abs(moveYneg)
            dirY = -1
        #Check to make sure non zero
        if(xFlag == 1):
            moveX = 0
            dirX = 0
        if(yFlag == 1):
            moveY = 0
            dirY = 0
        debounceMove = 1
    else:
        debounceMove += 1
    if(debounceMove > 4):
        debounceMove = 0


    #Decide movement
    if(debounce == 0):
        if(moveX > moveY):
            if(dirX == 1):
                pyautogui.press('right')
                print('right')
            if(dirX == -1):
                pyautogui.press('left')
                print('left')
        elif(moveY > moveX):
            if(dirY == 1):
                pyautogui.press('up')
                print('up')
            if(dirY == -1):
                pyautogui.press('down')
                print('down')

    #
    if button == 1:
        pyautogui.press('space')
