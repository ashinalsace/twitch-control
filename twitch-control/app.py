
from logging import NullHandler
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Tree
import twitchbot.bot as tw
import actions.actions as ac
import control.actions as cm

import os
from dotenv import load_dotenv
import time, threading

layout = [[sg.Text("Twitch Chat bot Machine Control")]]
window = None
runActions = False

def runCheck():
    global runActions
    print(time.ctime(), runActions)
    if (runActions):
        act = ac.choose_action()
        if (act != None):
            cm.executeAction(act)
    threading.Timer(2, runCheck).start()

def doButConnect():
    if (tw.doConnect(TWITCH_CHANNEL,TWITCH_NICKNAME,TWITCH_OAUTHTOKEN)):
        global window
        window["Connect"].update(disabled=True)
def doButStart():
    global runActions
    window["Start"].update(disabled=True)
    window["Stop"].update(disabled=False)
    runActions = True
def doButStop():
    global runActions
    window["Start"].update(disabled=False)
    window["Stop"].update(disabled=True)
    runActions = False
def doButExit():
    window.close()


buttons = {"Connect": doButConnect, "Start":doButStart, "Stop":doButStop, "Exit":doButExit}

# Load environment
load_dotenv()  # take environment variables from .env
TWITCH_CHANNEL = os.getenv('TWITCH_CHANNEL')
TWITCH_NICKNAME = os.getenv('TWITCH_NICKNAME')
TWITCH_OAUTHTOKEN = os.getenv('TWITCH_OAUTHTOKEN')


for but in buttons:
    layout.append([sg.Button(but)])   

# Create the window
window = sg.Window("Control", layout)
# Start actions timer
threading.Timer(2, runCheck).start()

# Create an event loop
while True:
    event, values = window.read()
    if event in buttons:
        buttons[event]()
    # End program if user closes window
    if event == sg.WIN_CLOSED:
        break

