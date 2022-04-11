#!/usr/bin/python3

import socket
import threading
import keyboard

# Library for colors
from colorama import init, Fore
from colorama import Back
from colorama import Style

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
print(Fore.YELLOW + '            Text | Client | Alpha 22.03.2022 | DragonFire Community')
print()
username = input('Username> ')

def handle_messages(connection: socket.socket):
    while True:
        try:
            msg = connection.recv(1024)

            if msg:
                print(msg.decode())
            else:
                connection.close()
                break

        except Exception as e:
            print(f'Error handling message from server: {e}')
            connection.close()
            break

def client() -> None:
    SERVER_ADDRESS = '26.7.90.168'
    SERVER_PORT = 7001

    while True:
        try:
            socket_instance = socket.socket()
            socket_instance.connect((SERVER_ADDRESS, SERVER_PORT))
            threading.Thread(target=handle_messages, args=[socket_instance]).start()

            print(f'Connected to {SERVER_ADDRESS}')

            while True:
                msg = input(f'{username}> ')

                outputMsg = username + ': ' + msg

                if msg == 'quit':
                    break

                socket_instance.send(outputMsg.encode())

            socket_instance.close()

        except Exception as e:
            print(Fore.RED + '[Error] The connection is lost. Reconnecting...')


if __name__ == "__main__":
    client()
