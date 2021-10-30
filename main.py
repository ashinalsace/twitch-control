
import PySimpleGUI as sg
from PySimpleGUI.PySimpleGUI import Tree
from bot import doAction, doConnect
import os
from dotenv import load_dotenv
import time, threading



runActions = False

def runCheck():
    global runActions
    print(time.ctime(), runActions)
    if (runActions):
        doAction()
    threading.Timer(2, runCheck).start()

def doButConnect():
    doConnect(TWITCH_CHANNEL,TWITCH_NICKNAME,TWITCH_OAUTHTOKEN)
def doButStart():
    global runActions
    runActions = True
def doButStop():
    global runActions
    runActions = False
def doButExit():
    window.close()


# Load environment
load_dotenv()  # take environment variables from .env
TWITCH_CHANNEL = os.getenv('TWITCH_CHANNEL')
TWITCH_NICKNAME = os.getenv('TWITCH_NICKNAME')
TWITCH_OAUTHTOKEN = os.getenv('TWITCH_OAUTHTOKEN')

buttons = {"Connect": doButConnect, "Start":doButStart, "Stop":doButStop, "Exit":doButExit}

layout = [[sg.Text("Twitch Chat bot Machine Control")]]

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

