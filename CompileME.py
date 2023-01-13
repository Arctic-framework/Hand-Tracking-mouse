import os

import cv2
from cvzone.HandTrackingModule import HandDetector
import keyboard
import pyautogui
import os.path
import  colorama
global X1
global Y1
Inputed_Password = ""
DATA_File = ""
Active_Directory = ""
#Resolution is QHD+ by default
MESHRANGE1 = 1
PERMALISTMESSAGE = []
PERMALIST = []
PERMALIST_Y = []
PERMAFINGERDATA = []
curF1calc_Y = []
#LCLICK makes the cursos do a left click on the mouse whenever that action is performed same for RCLICK
print('This code is property of Brytan Kelly.')
curMESHRANGE = 1
print('welcome to the ARCTIC.AI framework. Created by Brytan.M.Kelly 9/3/2022')
print( colorama.Fore.LIGHTCYAN_EX +  """░█████╗░██████╗░░█████╗░████████╗██╗░█████╗░  ░█████╗░██╗
██╔══██╗██╔══██╗██╔══██╗╚══██╔══╝██║██╔══██╗  ██╔══██╗██║
███████║██████╔╝██║░░╚═╝░░░██║░░░██║██║░░╚═╝  ███████║██║
██╔══██║██╔══██╗██║░░██╗░░░██║░░░██║██║░░██╗  ██╔══██║██║
██║░░██║██║░░██║╚█████╔╝░░░██║░░░██║╚█████╔╝  ██║░░██║██║
╚═╝░░╚═╝╚═╝░░╚═╝░╚════╝░░░░╚═╝░░░╚═╝░╚════╝░  ╚═╝░░╚═╝╚═╝



██████╗░██╗░░░██╗  ██████╗░██████╗░██╗░░░██╗████████╗░█████╗░███╗░░██╗  ██╗░░██╗███████╗██╗░░░░░██╗░░░░░██╗░░░██╗
██╔══██╗╚██╗░██╔╝  ██╔══██╗██╔══██╗╚██╗░██╔╝╚══██╔══╝██╔══██╗████╗░██║  ██║░██╔╝██╔════╝██║░░░░░██║░░░░░╚██╗░██╔╝
██████╦╝░╚████╔╝░  ██████╦╝██████╔╝░╚████╔╝░░░░██║░░░███████║██╔██╗██║  █████═╝░█████╗░░██║░░░░░██║░░░░░░╚████╔╝░
██╔══██╗░░╚██╔╝░░  ██╔══██╗██╔══██╗░░╚██╔╝░░░░░██║░░░██╔══██║██║╚████║  ██╔═██╗░██╔══╝░░██║░░░░░██║░░░░░░░╚██╔╝░░
██████╦╝░░░██║░░░  ██████╦╝██║░░██║░░░██║░░░░░░██║░░░██║░░██║██║░╚███║  ██║░╚██╗███████╗███████╗███████╗░░░██║░░░
╚═════╝░░░░╚═╝░░░  ╚═════╝░╚═╝░░╚═╝░░░╚═╝░░░░░░╚═╝░░░╚═╝░░╚═╝╚═╝░░╚══╝  ╚═╝░░╚═╝╚══════╝╚══════╝╚══════╝░░░╚═╝░░░""")
print('This is an exstension of the Arctic.AI framework that I made almost six months ago :)')
print('Press X tox activate the snapshot program or to program in a new signal')
print('Press R to save trained values to desktop')
Inputed_Password = pyautogui.password(title="Arctic ID Verification", text="Pleas enter your Arctic user ID")
Active_Directory = pyautogui.prompt(title="Directory Verification", text="Where do you want all saved files to go?")
Active_Directory = fr"{Active_Directory}"
if Inputed_Password == "Test":
    curLIST1 = []
    curLIST_Y = []
    DATA_X = []
    # webcam
    cap = cv2.VideoCapture(0)
    cap.set(3, 2560)
    cap.set(4, 1440)
    #MY FHD screens resolution is 1920
    #MY FHD screens resolution is 1080
    # detector for hands
    detector = HandDetector(maxHands=1, detectionCon=.7)
    while True:
        success, img = cap.read()
        # hand tracking
        hands, img = detector.findHands(img)
        DATA_X = []
        if hands:
            hand = hands[0]
            lmList = hand['lmList']
            for lm in lmList:
                DATA_X.extend(lm)
                ################################## pinch test which is disabled by default.
                INDEXFINGER = lmList[8]
                THUMB = lmList[4]
                THUMB = THUMB[1]
                INDEXFINGER = INDEXFINGER[1]
                WRIST = lmList[0]
                X1, Y1, Z1 = WRIST
                THUMB3 = lmList[4]
                X2, Y2, Z2 = THUMB3
                FINAL = abs(THUMB-INDEXFINGER)
            pyautogui.moveTo(X1, Y1)



    #################################Constant LM checker for Snapshot program.
            def CUR():
                global curLIST1
                global curFUP
                global REALFINGERSUP
                global SCORE
                curFCALMAIN = 0
                curFUP = detector.fingersUp(hand)
                curMESHPOINT = 0
                REALFINGERSUP = detector.fingersUp(hand)
                curLIST1 = []
                curLIST1.clear()
                for iy in range(20):
                    curF1calc = lmList[curFCALMAIN]
                    curF1calc_Y = curF1calc[1]
                    curF1calc = curF1calc[0]
                    curFCALMAIN += 1
                    for iz in range(20):
                        curMESHRANGE1 = lmList[curMESHPOINT]
                        curMESHRANGE2 = lmList[curMESHPOINT]
                        curMESHRANGE1 = curMESHRANGE1[0]
                        curMESHRANGE2 = curMESHRANGE2[1]
                        curLIST1.append((abs(int(curMESHRANGE1)-(int(curF1calc)))))
                        curLIST_Y.append((abs(int(curMESHRANGE2) - (int(curF1calc_Y)))))
                        curMESHPOINT += 1
                    curMESHPOINT = 0
                SSD = curLIST1
            ################################################# This code basicaly just asks the user to descrbe what hand signal they are doing and saves it to a list along with the landmark data.
            try:
                DIRECTORY = 1
                if keyboard.is_pressed('x'):
                    MESSAGE1=pyautogui.prompt(title='SNAPSHOT ACTIVATED', text='what is your sign', default='')
                    LIST1 = []
                    LIST_Y = []
                    LIST_Y.clear()
                    LIST1.clear()
                    LIST_Y = curLIST_Y
                    LIST1 = curLIST1
                    F1 = LIST1[DIRECTORY]
                    F1_Y = LIST_Y[DIRECTORY]
                    PERMALIST.append(LIST1)
                    PERMALIST_Y.append(LIST_Y)
                    PERMALISTMESSAGE.append(MESSAGE1)
                    curFUP = detector.fingersUp(hand)
                    PERMAFINGERDATA.append(curFUP)

                SCORE = 0
                for iz in range(400):
                    F1 = LIST1[DIRECTORY]
                    F1_Y = LIST_Y[DIRECTORY]
                    F2 = curLIST1[DIRECTORY]
                    F2_Y = curLIST_Y[DIRECTORY]
                    if F1-100 <= F2:
                        if F1+100 >= F2:
                            SCORE += 1
                    if F1_Y-1000 <= F2_Y:
                        if F1_Y+1000 >= F2_Y:
                            SCORE += 10
                if SCORE < 100:
                    cv2.putText(img, "welp thats it", (100, 100), cv2.FONT_HERSHEY_COMPLEX,
                                5, (255, 0, 255), 5)






                    DIRECTORY += 1
                SCORE = 0
            except:
                print('')

    ################################################### The Render Function basicaly just tests for all of the points and if they match the saved points displays the text.
            def RENDER(DATA_X, DATA_Y, USE_FINGER_DATA, FINGER_UP_DATA, MESSAGE, RANGE_X, RANGE_Y):
                try:
                    SCORE = 0
                    DIRECTORY = 1
                    for iz in range(400):
                        F1 = DATA_X[DIRECTORY]
                        F1_Y = DATA_Y[DIRECTORY]
                        F2 = curLIST1[DIRECTORY]
                        F2_Y = curLIST_Y[DIRECTORY]
                        if F1 - RANGE_X <= F2:
                            if F1 + RANGE_X >= F2:
                                SCORE += 1
                        if F1_Y - RANGE_Y<= F2_Y:
                            if F1_Y + RANGE_Y >= F2_Y:
                                SCORE += 1
                        if USE_FINGER_DATA == False:
                            if SCORE > 790:
                                cv2.putText(img, MESSAGE, (100, 100), cv2.FONT_HERSHEY_COMPLEX,
                                            5, (255, 0, 255), 5)
                                if MESSAGE == "LCLICK":
                                    pyautogui.leftClick()
                                if MESSAGE == "RCLICK":
                                    pyautogui.rightClick()
                        if USE_FINGER_DATA == True:
                            if SCORE > 790:
                                if curFUP == FINGER_UP_DATA:
                                    cv2.putText(img, MESSAGE, (100, 100), cv2.FONT_HERSHEY_COMPLEX,
                                            5, (255, 0, 255), 5)
                                    if MESSAGE == "LCLICK":
                                        pyautogui.leftClick()
                                    if MESSAGE == "RCLICK":
                                        pyautogui.rightClick()






                        else:
                           print("")
                        DIRECTORY += 1
                    SCORE = 0
                except:
                    print("")

    ################################################################################### renders cur or current finger position always.
            CUR()
            try:
                    ######### always trys too render certain gestures and checks millions of points of DATA_X and DATA_Y because I was too lazy too implement a pretrained algorythim.
                for i in range(len(PERMALIST)):
                    RENDERME = PERMALIST[RENDERDIRECTORY]
                    RENDERME_Y = PERMALIST_Y[RENDERDIRECTORY]
                    RENDER(RENDERME, RENDERME_Y, True, PERMAFINGERDATA[RENDERDIRECTORY], PERMALISTMESSAGE[RENDERDIRECTORY], 70, 70) # this should be 40, 40 for small data sets the larger tha data set the smaller it should be 25, 25 for larger data sets
                    RENDERDIRECTORY += 1
                RENDERDIRECTORY = 0
            except:
                print(f'')

        cv2.imshow('image', img)
        cv2.waitKey(1)
        if keyboard.is_pressed("r"):

            #save_path = (r'C:\Users\jenna\OneDrive\Desktop')
            save_path = (Active_Directory)

            name_of_file = ("Saved_Handtracking_Data")

            completeName = os.path.join(save_path, name_of_file + ".txt")

            file1 = open(completeName, "w")

            toFile = f"{PERMALIST, PERMALIST_Y}"

            file1.write(toFile)

            file1.close()
            print("Saved successfully")

else:
    print("Wrong password")
    print("""░██████╗░░█████╗░░█████╗░██████╗░██████╗░██╗░░░██╗███████╗
██╔════╝░██╔══██╗██╔══██╗██╔══██╗██╔══██╗╚██╗░██╔╝██╔════╝
██║░░██╗░██║░░██║██║░░██║██║░░██║██████╦╝░╚████╔╝░█████╗░░
██║░░╚██╗██║░░██║██║░░██║██║░░██║██╔══██╗░░╚██╔╝░░██╔══╝░░
╚██████╔╝╚█████╔╝╚█████╔╝██████╔╝██████╦╝░░░██║░░░███████╗
░╚═════╝░░╚════╝░░╚════╝░╚═════╝░╚═════╝░░░░╚═╝░░░╚══════╝""")