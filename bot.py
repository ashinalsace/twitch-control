# Imports-----------------------------------------------------
from typing import Match
import twitch
import os
from dotenv import load_dotenv
import pyautogui
import sched, time, operator
# Global------------------------------------------------------
actions = ["up","down"]
actionsCount = {"up":0, "down":0,}
scheculeAction = sched.scheduler(time.time, time.sleep)
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
    if (action == "echo!"):
        pyautogui.write(action, interval=0.25)
        pyautogui.keyDown('enter')
#-------------------------------------------------------------
def do_Action(sc): 
    print("Chose action")
    # Get ordered list
    sorted_actions = sorted(actionsCount.items(), key=operator.itemgetter(1),reverse=True)
    print('Actions in ascending order by value : ',sorted_actions)
    actionSelected = sorted_actions[0][0]
    if (actionsCount[actionSelected] > 0):
        executeAction(actionSelected)
    # Reschedule timer
    actionsCount[actionSelected] = 0
    scheculeAction.enter(5, 1, do_Action, (sc,))
# Main--------------------------------------------------------

load_dotenv()  # take environment variables from .env
TWITCH_CHANNEL = os.getenv('TWITCH_CHANNEL')
TWITCH_NICKNAME = os.getenv('TWITCH_NICKNAME')
TWITCH_OAUTHTOKEN = os.getenv('TWITCH_OAUTHTOKEN')


print ("Connecting to channel",  TWITCH_CHANNEL)



twitch.Chat(channel=TWITCH_CHANNEL, nickname=TWITCH_NICKNAME, oauth=TWITCH_OAUTHTOKEN).subscribe(
        lambda message: 
            parseMessage(message.text)
        )

scheculeAction.enter(2, 1, do_Action, (scheculeAction,))
scheculeAction.run()

