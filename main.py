
import PySimpleGUI as sg
from bot import doAction, doConnect
import os
from dotenv import load_dotenv
import time, threading


run = False

def runCheck():
    print(time.ctime())
    if(run):
        print("Running")
        doAction()
    else:
         print("Not running")
    threading.Timer(2, runCheck).start()

# Load environment
load_dotenv()  # take environment variables from .env
TWITCH_CHANNEL = os.getenv('TWITCH_CHANNEL')
TWITCH_NICKNAME = os.getenv('TWITCH_NICKNAME')
TWITCH_OAUTHTOKEN = os.getenv('TWITCH_OAUTHTOKEN')

layout = [[sg.Text("Twitch Chat bot Machine Control")],
    [sg.Button("Connect")],
    [sg.Button("Start")], 
    [sg.Button("Stop")],
    [sg.Button("OK")]]

# Create the window
window = sg.Window("Control", layout)
threading.Timer(2, runCheck).start()

# Create an event loop
while True:
    event, values = window.read()
    # End program if user closes window or
    # presses the OK button
    if event == "OK" or event == sg.WIN_CLOSED:
        break
    if event =="Connect":
        doConnect(TWITCH_CHANNEL,TWITCH_NICKNAME,TWITCH_OAUTHTOKEN)
    if event =="Start":
        run = True
        print("Started")
    if event =="Stop":
        run = False
        print("Stopped")

window.close()