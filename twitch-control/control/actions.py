# Imports-----------------------------------------------------
import pyautogui
# Global-----------------------------------------------------
mouseMove = { "up":(0,-10), "down":(0, 10), "left":(-10, 0), "right":(10,0)}
#-------------------------------------------------------------
def executeAction(action):
    print("Exceuting", action)
    if (action in mouseMove):
        pyautogui.move(mouseMove[action])
    if (action == "click"):
       pyautogui.click()
    if (action == "echo"):
        pyautogui.write(action, interval=0.25)
        pyautogui.keyDown('enter')
