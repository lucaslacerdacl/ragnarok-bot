import pyautogui
import time
from datetime import datetime as dt

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
    pyautogui.drag(distance, 0, duration=0.5)

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

    pyautogui.typewrite('@go 11', interval=0.5)
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
    pyautogui.typewrite('2500', interval=0.5)
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

def getMousePos():
    pos = pyautogui.position()
    print(pos)

def go():
    print("Change window")
    time.sleep(5)
    rechargePattern()

    while(True):
        farmPattern()
        minute = dt.now().minute
        if(minute == 30 or minute == 0):
            rechargePattern()
