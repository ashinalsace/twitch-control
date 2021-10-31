# Imports-----------------------------------------------------
from typing import Match
import twitch
import actions.actions as ac

# Global------------------------------------------------------

#Functions----------------------------------------------------
def parseMessage(text):
    print(text)
    ac.record_action(text)

def doConnect(TWITCH_CHANNEL,TWITCH_NICKNAME,TWITCH_OAUTHTOKEN):
    # Connect to chat feed
    print ("Connecting to channel",  TWITCH_CHANNEL)
    bConnected = twitch.Chat(channel=TWITCH_CHANNEL, nickname=TWITCH_NICKNAME, oauth=TWITCH_OAUTHTOKEN).subscribe(
        lambda message: 
            parseMessage(message.text)
    )
    return bConnected



