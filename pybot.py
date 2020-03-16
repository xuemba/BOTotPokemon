#Target? fishing

import pyautogui
import time
import threading
import keyboard

def fish():
    while 1:
        #time.sleep(1)
        x = pyautogui.locateCenterOnScreen('C:\\Users\\lucas\\Desktop\\OTP BOt\\pesca.png', confidence=.9)
        print('antes do while',x)
        if x!=None:
            print('entrou')
            pyautogui.press('f12')
            #time.sleep(0.5)
            pyautogui.click()

            pyautogui.press('f12')
            pyautogui.click()
            x=None

def autoAttack():    
    pyautogui.press('f1')
    pyautogui.press('f2')
    pyautogui.press('f3')
    pyautogui.press('f4')
    pyautogui.press('f5')
    pyautogui.press('f6')
    pyautogui.press('f7')
    pyautogui.press('f8')
    pyautogui.press('f9')
    pyautogui.press('f10')


if __name__ == "__main__":
    time.sleep(4)
    while 1:
        if keyboard.is_pressed('q'):
            autoAttack()
        if keyboard.is_pressed('p'):
            fish()
        if pyautogui.locateOnScreen('C:\\Users\\lucas\\Desktop\\OTP BOt\\haste.PNG',grayscale=True, confidence=.9) == None:
            pyautogui.press('f11')
