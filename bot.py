# Imports-----------------------------------------------------
from typing import Match
import twitch
import sched, time, operator
import pyautogui

# Global------------------------------------------------------
actions = ["up","down", "left", "right", "click", "echo"]
actionsCount = {"up":0, "down":0, "left":0, "right":0, "click":0, "echo":0,}
scheculeAction = sched.scheduler(time.time, time.sleep)
bConnected = False

#Functions----------------------------------------------------
def parseMessage(text):
    print(text)
    if text in actions:
        print(text, "found in ", actions)
        actionsCount[text] = actionsCount[text] + 1
    print(actionsCount)

#-------------------------------------------------------------
def executeAction(action):
    print("Exceuting", action)
    if (action == "up"):
        pyautogui.move(0, -10)
    if (action == "down"):
       pyautogui.move(0, 10)
    if (action == "left"):
       pyautogui.move(-10, 0)
    if (action == "right"):
       pyautogui.move(10, 0)
    if (action == "click"):
       pyautogui.click()
    if (action == "echo"):
        pyautogui.write(action, interval=0.25)
        pyautogui.keyDown('enter')

#-------------------------------------------------------------
def doAction(): 
    print("Choose action")
    # Get ordered list
    sorted_actions = sorted(actionsCount.items(), key=operator.itemgetter(1),reverse=True)
    print('Actions in ascending order by value : ',sorted_actions)
    actionSelected = sorted_actions[0][0]
    if (actionsCount[actionSelected] > 0):
        executeAction(actionSelected)
    # Reschedule timer
    for act in actionsCount:
        actionsCount[act] = 0

def doConnect(TWITCH_CHANNEL,TWITCH_NICKNAME,TWITCH_OAUTHTOKEN):
    # Connect to chat feed
    print ("Connecting to channel",  TWITCH_CHANNEL)
    bConnected = twitch.Chat(channel=TWITCH_CHANNEL, nickname=TWITCH_NICKNAME, oauth=TWITCH_OAUTHTOKEN).subscribe(
        lambda message: 
            parseMessage(message.text)
    )
    return bConnected



