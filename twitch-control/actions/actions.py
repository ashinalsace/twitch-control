# Imports-----------------------------------------------------
import operator

# Global------------------------------------------------------
actionsCount = {"up":0, "down":0, "left":0, "right":0, "click":0, "echo":0,}
actions = ["up","down", "left", "right", "click", "echo"]
#Functions----------------------------------------------------
def record_action(action):
    print(action)
    if action in actions:
        print("Found action ", action )
        actionsCount[action] = actionsCount[action] + 1
    print(actionsCount)
#-------------------------------------------------------------
def choose_action(): 
    chosenAction = None
    print("Choose action")
    # Get ordered list
    sorted_actions = sorted(actionsCount.items(), key=operator.itemgetter(1),reverse=True)
    print('Actions in ascending order by value : ',sorted_actions)
    firstAction = sorted_actions[0][0]
    if (actionsCount[firstAction] > 0):
        chosenAction = firstAction
    # Reset data
    for act in actionsCount:
        actionsCount[act] = 0
    return chosenAction




