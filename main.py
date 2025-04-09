import cv2
import pydirectinput
import numpy as np
import pyautogui
import time
import os
import pyscreeze

def outOfBloodies():
    return True

def check_mysteryboxes(file, file_paths, purchase_location):
    if purchase_location is not None:
        for i in purchase_location:
            y = i[0]
            i = pyautogui.center(i)
            x = i[1]
            print(pyautogui.pixel(int(x), int(y)))
            if file_paths[file]["amount"] != []:
                for k in file_paths[file]["amount"]:
                    point1 = np.array(i)
                    point2 = np.array(k)
                    distance = np.linalg.norm(point2 - point1)
                    if distance >= 10:
                        file_paths[file]["amount"].append(i)
            else:
                file_paths[file]["amount"].append(i)

def purchaseableItems():
    pyautogui.screenshot('my_screenshot.png')

    file_paths = {}
    for folder, subfolders, filenames in os.walk('icons'):
        for filename in filenames:
            file_path = os.path.join(folder, filename)
            file_paths[filename[:-4]] = {"filepath": file_path, "folder": folder, "amount": []}

    for file in file_paths.keys():
        try:
            confidence_level = 0
            if file_paths[file]["folder"] in ["icons\\offerings\\fog"]:
                confidence_level = 0.97
            elif file_paths[file]["folder"] in ["icons\\items"]:
                confidence_level = 0.95
            elif file_paths[file]["folder"] in ["icons\\items\\flashlight"]:
                confidence_level = 0.80
            else:
                confidence_level = 0.90

            purchase_location = pyautogui.locateAll(file_paths[file]["filepath"], "my_screenshot.png", confidence=confidence_level)
            purchase_location = list(purchase_location)

        except pyscreeze.ImageNotFoundException as e:
            purchase_location = None
        
        if purchase_location is not None:
            for i in purchase_location:
                y = i[1]
                i = pyautogui.center(i)
                x = i[0]
                if file == "brown_mystery_box":
                    if not (pyautogui.pixelMatchesColor(int(x), int(y), (56, 43, 33), tolerance=20) or pyautogui.pixelMatchesColor(int(x), int(y), (92, 68, 50), tolerance=20)): # Non-grayed out: (92, 68, 50)
                        continue
                elif file == "yellow_mystery_box":
                    if not (pyautogui.pixelMatchesColor(int(x), int(y), (106, 87, 29), tolerance=20) or pyautogui.pixelMatchesColor(int(x), int(y), (203, 164, 45), tolerance=20)): # (203, 164, 45)
                        continue
                elif file == "green_mystery_box":
                    if not pyautogui.pixelMatchesColor(int(x), int(y), (15, 106, 27), tolerance=50):
                        # print(pyautogui.pixel(int(x), int(y)))
                        continue
                elif file == "purple_mystery_box":
                    if not pyautogui.pixelMatchesColor(int(x), int(y), (77, 38, 81), tolerance=20):
                        continue
                elif file == "pink_mystery_box":
                    if not pyautogui.pixelMatchesColor(int(x), int(y), (0, 0, 0), tolerance=10):
                        continue

                if file_paths[file]["amount"] != []:
                    for k in file_paths[file]["amount"]:
                        point1 = np.array(i)
                        point2 = np.array(k)
                        distance = np.linalg.norm(point2 - point1)
                        if distance >= 10:
                            file_paths[file]["amount"].append(i)
                else:
                    file_paths[file]["amount"].append(i)
    
    return file_paths

    # for file in file_paths:
    #     if file_paths[file]["amount"] != []:
    #         for i in file_paths[file]["amount"]:
    #             print(file)
    # print("============")
    # for i in file_paths:
    #     for k in file_paths[i]["amount"]:
    #         pyautogui.moveTo(k)
    #         print(i)
    #         time.sleep(.5)




def selectPurchase(file_paths, prioList):
    for item in prioList:
        for file in file_paths:
            if file == item and file_paths[file]["amount"] != []:
                for val in file_paths[file]["amount"]:
                    time.sleep(2)
                    pyautogui.moveTo(val)
                    pyautogui.mouseDown()
                    time.sleep(0.1)
                    pyautogui.mouseUp()


def pickPriority():
    # Improve on system later, create a way to interact with fileIO, allow CLI question system for list
    prioList = ["bloodsense_map", "bloodshot_eye", "anti_hemorrhagic_syringe", "brand_new_part", "odd_bulb", "brown_mystery_box", "green_mystery_box", "purple_medkit", "jigsaw_piece", "auto_purchase"]
    return prioList


def main():
    for i in range(3):
        time.sleep(1)
        print(i)
    
    while True:
        file_paths = purchaseableItems()
        prioList = pickPriority()
        selectPurchase(file_paths, prioList)
        time.sleep(2)
        pyautogui.moveTo(0, 1000)
    

if __name__ in "__main__":
    main()