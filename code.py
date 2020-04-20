import pyautogui
import time
from datetime import datetime as dt
from PIL import Image, ImageChops, ImageGrab
import pytesseract

pytesseract.pytesseract.tesseract_cmd = r'C:\\Program Files\\Tesseract-OCR\\tesseract.exe'

def shoot():
    time.sleep(.3)
    pyautogui.press('f1')
    time.sleep(.3)
    pyautogui.press('f1')
    time.sleep(.3)

def teleport():
    pyautogui.press('f2')

def leftClick(posX, posY):
    pyautogui.doubleClick(x=posX, y=posY, button='left')
    pyautogui.mouseDown()
    pyautogui.mouseUp()

def pressEnter():
    pyautogui.keyDown('enter')
    pyautogui.keyUp('enter')

def drag(posX, posY, distance):
    pyautogui.click(x=posX, y=posY, button='left')
    pyautogui.drag(distance, 0, duration=0.3)

def farmPattern():
    teleport()

    shoot()
    leftClick(1107, 678)
    time.sleep(.3)
    
    leftClick(913, 764)
    time.sleep(.3)
    
    leftClick(688, 628)
    time.sleep(.3)
    shoot()

    leftClick(913, 764)
    time.sleep(.3)

    leftClick(688, 628)
    time.sleep(.3)
    shoot()

def teleportToGonryun():
    pressEnter()
    time.sleep(0.75)

    pyautogui.typewrite('@go 11', interval=0.1)
    time.sleep(0.75)
    pressEnter()

    time.sleep(2)
    pressEnter()

def talkToKafra():
    
    leftClick(915, 442)
    time.sleep(1)

    pressEnter()
    time.sleep(1)

    pyautogui.keyDown('down')
    pyautogui.keyUp('down')
    time.sleep(1)

    pressEnter()
    time.sleep(1)

    pressEnter()
    time.sleep(1)

def heal():
    leftClick(702, 479)
    time.sleep(1)

def toggleItems():
    leftClick(98, 185)
    time.sleep(1)

def closeInventory():
    leftClick(956, 876)
    time.sleep(1)

def getFly():
    drag(759, 455, 300)
    pyautogui.typewrite('250', interval=0.5)
    pressEnter()

def getAmmo():
    leftClick(716, 606)
    time.sleep(1)
    drag(759, 616, 300)
    pyautogui.typewrite('5000', interval=0.5)
    pressEnter()

def goToAbyss():
    leftClick(1159, 512)
    time.sleep(1)
    pressEnter()
    time.sleep(2)
    
    leftClick(929, 223)
    time.sleep(1)
    shoot()

def rechargePattern():
    teleportToGonryun()
    heal()
    talkToKafra()
    toggleItems()
    getFly()
    getAmmo()
    toggleItems()
    closeInventory()
    goToAbyss()

def inMacroRoom():
    find = pyautogui.locateOnScreen('./antiMacro.png', confidence=.9)
    return find != None

def getNumberFromImage():
    time.sleep(1)
    box = (215, 155, 315, 205)
    im = ImageGrab.grab(box)
    text = pytesseract.image_to_string(im)
    return text
    
        
def typeNumber():
    number = getNumberFromImage()
    if (len(number.split('\n')) > 1):
        onlyNumber = number.split('\n')[1]
        pyautogui.typewrite(onlyNumber, interval=0.5)
        time.sleep(5)
        
        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

        pyautogui.keyDown('enter')
        pyautogui.keyUp('enter')

def inAbyss():
    find = pyautogui.locateOnScreen('./abyssMap.png', confidence=.8)
    return find != None

def goBackToAbyss():
    teleportToGonryun()
    heal()
    goToAbyss()
    
def getMousePos():
    pos = pyautogui.position()
    print(pos)

def go():
    print("Change window")
    time.sleep(5)

    
    while(True):
        amIInAbyss = inAbyss()
        amIInMacroRoom = inMacroRoom()
        
        if (not amIInAbyss and not amIInMacroRoom):
            goBackToAbyss()

        if (amIInMacroRoom):
            typeNumber()
        else:
            farmPattern()

            minute = dt.now().minute
            if(minute == 45):
                rechargePattern()
