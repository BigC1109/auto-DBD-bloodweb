import cv2
import pydirectinput
import numpy as np
import pyautogui
import time
import os
import pyscreeze

'''
This program will prioritize purchasing items in the bloodweb for Dead By Daylight.
It does this through image recognition of pyautogui. Automatically picking the wanted
item first, and when that is completed purchases the automatic purchase button.
'''

def outOfBloodies():
    '''
    Future failsafe for when out of bloodpoints, will just end the program.
    '''
    return False

def purchaseableItems(priolist):
    '''
    This will go through each icon on the screen, and determine what is purchaseable.
    It will add it to the dictionary file_paths, where it stores the amount of each item
    there is.
    '''
    pyautogui.screenshot('my_screenshot.png')

    file_paths = {}
    for folder, subfolders, filenames in os.walk('icons'):
        for filename in filenames:
            print(filenames)
            if filename in priolist:
                print("\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n\n")
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

                # This specific section was made because the mystery_box's look too similar, and need to be color tested as well.
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
                    if not pyautogui.pixelMatchesColor(int(x), int(y), (209, 13, 111), tolerance=10):
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

def selectPurchase(file_paths, prioList):
    '''
    This will collect the current prioList, and parse through it using the file_paths from earlier.
    Using both of these it will purchase items in order of what the user wants.
    '''
    for item in prioList:
        print(f"item = {item}")
        print(f"paths = {file_paths}")
        for file in file_paths:
            if file == item and file_paths[file]["amount"] != []:
                for val in file_paths[file]["amount"]:
                    time.sleep(2)
                    pyautogui.moveTo(val)
                    pyautogui.mouseDown()
                    time.sleep(0.1)
                    pyautogui.mouseUp()


def pickPriority():
    '''
    In the future this will check for the pickprio.csv file, if it exists will get the information from it.
    If it doesn't exist, it will run through and create one through CLI command prompts.
    '''
    # prioList = ["bloodsense_map", "bloodshot_eye", "anti_hemorrhagic_syringe", "brand_new_part", "odd_bulb", "brown_mystery_box", "green_mystery_box", "purple_medkit", "jigsaw_piece", "auto_purchase"]
    prioList = ["iconAddon_iridescentBlightTag.png", "iconAddon_compoundThirtyThree.png", "bloody_party_streamers.png", "iconAddon_blightedCrow.png", "iconAddon_blightedRat.png"]
    # prioList = []
    user_input = "None"
    while True:
        # This will get better over time I promise Ian hahaha
        user_input = input("Enter the name of an item to add it to the list. Make sure it is all lowercase, and uses _ instead of spaces\n")
        if user_input == "":
            break
        else:
            prioList.append(user_input)
    
    prioList.append("auto_purchase.png")

        
    return prioList


def main():

    prioList = pickPriority()

    for i in range(3):
        time.sleep(1)
        print(i)

    while not outOfBloodies():
        file_paths = purchaseableItems(prioList)
        selectPurchase(file_paths, prioList)
        time.sleep(2)
        pyautogui.moveTo(0, 1000)
    

if __name__ in "__main__":
    main()