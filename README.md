# Twitch chat bot for keyboard control

This is a working application that allows messages sent in a twitch chat feed to translate in to key presses on the machine running the script

Simple implementation thanks to the packages twitch-python https://pypi.org/project/twitch-python/ and PyAutoGUI https://pypi.org/project/PyAutoGUI/

## Installation

```sh
$ pip install -r requirements.txt
$ python.exe .\app.py
```
# Usage

All settings are in settings.json

- commandactions: This is a map of the message on the chat and the corresponding keyboard action.
- actionPeriod: How ofte,n in seconds, the actions should be run
- channel: The twitch channel 
- nickname: Nickname of twitch user
- token: oAuth token to connect to the twitch chat

To generate token for chat, I used https://twitchapps.com/tmi/ but I am not responsible for this site. After logging to the site,  copy the token auth:... in to the settings.json file.

The application records all commands send on chat and selects most popular during the last run period to be executed
## Next Steps
- Only ever tested on Windows with Python 3.8
- Add mouse control
- Only accept commands from certain users
