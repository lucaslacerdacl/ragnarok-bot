from PIL import ImageGrab
import os
import time
 
def screenGrab():
    box = (425,118,1450,887)
    im = ImageGrab.grab(box)
    im.save(os.getcwd() + '\\full_snap__' + str(int(time.time())) + '.png', 'PNG')
 
def main():
    screenGrab()
 
if __name__ == '__main__':
    main()
