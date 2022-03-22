#!/usr/bin/python3

# Vars
connectURL = 'http://26.194.160.135:7001/'
errorText = "Error occured! Server is not responsing"
errorInput = 'Press ENTER to continue'

# System vars (DON'T TOUCH IT)
readMsgDisabled = False

#Libs
import requests # Requests

# Library for colors
from colorama import init, Fore
from colorama import Back
from colorama import Style

# Required for keybinds
import keyboard

# Init methods
init(autoreset=True)

# Logo
print('██████╗ ███╗   ███╗███████╗███████╗███████╗███████╗███╗   ██╗ ██████╗ ███████╗██████╗')
print('██╔══██╗████╗ ████║██╔════╝██╔════╝██╔════╝██╔════╝████╗  ██║██╔════╝ ██╔════╝██╔══██╗')
print('██║  ██║██╔████╔██║█████╗  ███████╗███████╗█████╗  ██╔██╗ ██║██║  ███╗█████╗  ██████╔╝')
print('██║  ██║██║╚██╔╝██║██╔══╝  ╚════██║╚════██║██╔══╝  ██║╚██╗██║██║   ██║██╔══╝  ██╔══██╗')
print('██████╔╝██║ ╚═╝ ██║███████╗███████║███████║███████╗██║ ╚████║╚██████╔╝███████╗██║  ██║')
print('╚═════╝ ╚═╝     ╚═╝╚══════╝╚══════╝╚══════╝╚══════╝╚═╝  ╚═══╝ ╚═════╝ ╚══════╝╚═╝  ╚═╝')
print()
print(Fore.YELLOW + '           Text | Client | Alpha 22.03.2022 | DragonFire Community')

usernameToLogin = input('Username> ')

def sendMessageToServer():
    readMsgDisabled = True

    msgToSend = input('Message> ')
    while True:
        try:
            requests.post(connectURL + 'api/v1/message/send', headers = {"username": usernameToLogin, "messageToSend": msgToSend})
            readMsgDisabled = False
            break
        except requests.exceptions.ConnectionError:
            print('[Error] The connection is lost. Reconnecting...')

while True:
    if keyboard.is_pressed('q'): sendMessageToServer()
    else:
        try:
            messages = requests.get(connectURL + 'api/v1/message/messages')
            print(messages.text)
        except requests.exceptions.ConnectionError:
            print('[Error] The connection is lost. Reconnecting...')