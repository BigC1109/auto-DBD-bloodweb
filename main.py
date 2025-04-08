import cv2
import pydirectinput
import numpy as np
import pyautogui
import time
import os

def outOfBloodies():
    return True

def purchaseableItems():
    pyautogui.screenshot('my_screenshot.png')

    file_paths = {}
    for folder, subfolders, filenames in os.walk('icons'):
        for filename in filenames:
            file_path = os.path.join(folder, filename)
            file_paths[filename.strip('.png')] = {"filepath": file_path, "amount": []}
    for key in file_paths.keys():
        print(file_paths[key]["filepath"])

    for file in file_paths.keys():
        try:
            purchase_location = pyautogui.locateAll(file_paths[file]["filepath"], "my_screenshot.png", confidence=0.7)
            purchase_location = list(purchase_location)
        except Exception as e:
            print(e)
            purchase_location = None
        
        if purchase_location is not None:
            print("Success!")
            for i in purchase_location:
                i = pyautogui.center(i)
                if file_paths[file]["amount"] != []:
                    for k in file_paths[file]["amount"]:
                        point1 = np.array(i)
                        point2 = np.array(k)
                        distance = np.linalg.norm(point2 - point1)
                        if distance >= 10:
                            file_paths[file]["amount"].append(i)
                else:
                    file_paths[file]["amount"].append(i)
        else:
            print("failure!")
    
    print(file_paths)

    for i in file_paths:
        for k in file_paths[i]["amount"]:
            pyautogui.moveTo(k)
            pyautogui.mouseDown()
            time.sleep(0.2)
            pyautogui.mouseUp()
            time.sleep(3)




def selectPurchase():
    pyautogui.screenshot('my_screenshot.png')

    file_paths = []
    for folder, subfolders, filenames in os.walk('icons'):
        for filename in filenames:
            file_path = os.path.join(folder, filename)
            file_paths.append(file_path)
    print(file_paths)

    try:
        purchase_location = pyautogui.locate("image.png", "my_screenshot.png", confidence=0.7)
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
    for i in range(0):
        time.sleep(1)
        print(i)
    
    # selectPurchase()
    purchaseableItems()
    

if __name__ in "__main__":
    main()