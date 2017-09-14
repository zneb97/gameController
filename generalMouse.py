import pyautogui
import sys
import arduinoSerial

debounce = 0;

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

    if x>10:
        moveX = translate(x, 10, 80, 1, 40)
    elif x<-30:
        moveX = translate(x, -145, -30, -40, -1)
    else:
        moveX = 0
    if y>30:
        moveY = translate(y, 30, 192, -1, -40)
    elif y<-30:
        moveY = translate(y, -126, -30, 40, 1)
    else:
        moveY = 0

    pyautogui.moveRel(moveX,moveY)


    if(debounce == 0):
            if button == 1:
                pyautogui.click()
                debounce = 1;
    else:
        debounce += 1

    if(debounce>3):
        debounce = 0
