import os, json, time
from os import path
import operator
import pyautogui
import twitch

# Global
actionMappings = {}
commandCounts = {}

#Functions----------------------------------------------------
def record_command(command):
    print("Received ",command)
    if command in commandCounts:
        commandCounts[command] = commandCounts[command] + 1
        print("Added command ", command)
#-------------------------------------------------------------
def choose_action(): 
    chosenAction = None
    print("Choosing action from ", commandCounts)
    # Get ordered list
    sorted_commands = sorted(commandCounts.items(), key=operator.itemgetter(1),reverse=True)
    firstCommand = sorted_commands[0][0]
    if (commandCounts[firstCommand] > 0):
        chosenAction = actionMappings[firstCommand]
        print("Chosen ", chosenAction)
    else:
        print("No action chosen")
    # Reset counts
    for cmd in commandCounts:
        commandCounts[cmd] = 0
    return chosenAction
#------------------------------------------------------------
def load_commands(commands):
    for command in commands:
        actionMappings[command] = commands[command]
        commandCounts[command] = 0
    print("Loaded commands ", actionMappings)
#------------------------------------------------------------
def runActionSelection():
    print("Checking for actions: ", time.ctime())
    action = choose_action()
    if (action != None):
        pyautogui.write(action, interval=0.25)
#------------------------------------------------------------
def main():
    SETTINGS_FILE = path.join(path.dirname(__file__), r'settings.json')
    with open(SETTINGS_FILE) as json_settings_file:
        settings = json.load(json_settings_file)

    load_commands(settings["commandactions"])

    twitch.Chat(channel=settings["channel"], 
                nickname=settings["nickname"], 
                oauth=settings["token"]).subscribe(
        lambda message:
            record_command(message.text))

    try:
        while True:
            time.sleep(settings["actionPeriod"])
            print("Running. Hit Ctrl-C to quit")
            runActionSelection()
    except:
        pass            

if __name__ == '__main__':
    main()