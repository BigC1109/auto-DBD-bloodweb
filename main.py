import cv2
import pydirectinput
import numpy as np
import pyautogui
import time
import os

LOCALPATH = "C:\\Users\\Jeffr\\OneDrive\\Desktop\\projects\\auto-DBD-bloodweb\\"

def outOfBloodies():
    return True

def selectPurchase():
    os.remove('my_screenshot.png')
    if True:
        os.remove('region_screenshot.png')
    pyautogui.screenshot('my_screenshot.png')

    try:
        purchase_location = pyautogui.locate("image.png", "my_screenshot.png", confidence=0.1)
    except pyautogui.ImageNotFoundException as e:
        purchase_location = None
    
    if purchase_location is not None:
        print("Success!")
        purchase_location = pyautogui.center(purchase_location)
        pyautogui.click(purchase_location)
    else:
        print("failure!")

def pickPriority():
    pass

def main():
    for i in range(5):
        time.sleep(1)
        print(i)
    
    selectPurchase()
    

if __name__ in "__main__":
    main()