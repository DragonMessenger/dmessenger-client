#!/usr/bin/python3

# Library for colors
from colorama import init, Fore
from colorama import Back
from colorama import Style

recieveBytes = 2048

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
print(Fore.YELLOW + '           Voice | Client | Alpha 22.03.2022 | DragonFire Community')

import socket
import threading
import pyaudio

class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        
        while 1:
            try:
                self.target_ip = '26.194.160.135'
                self.target_port = 7002

                self.s.connect((self.target_ip, self.target_port))

                break
            except:
                print(Fore.RED + '[Error] The connection is lost. Reconnecting...')

        chunk_size = 1024 # 512
        audio_format = pyaudio.paInt16
        channels = 1
        rate = 20000

        # initialise microphone recording
        self.p = pyaudio.PyAudio()
        self.playing_stream = self.p.open(format=audio_format, channels=channels, rate=rate, output=True, frames_per_buffer=chunk_size)
        self.recording_stream = self.p.open(format=audio_format, channels=channels, rate=rate, input=True, frames_per_buffer=chunk_size)
        
        print(Fore.CYAN + "Connected to Server")

        # start threads
        receive_thread = threading.Thread(target=self.receive_server_data).start()
        self.send_data_to_server()

    def receive_server_data(self):
        while True:
            try:
                data = self.s.recv(recieveBytes)
                self.playing_stream.write(data)
            except:
                pass


    def send_data_to_server(self):
        while True:
            try:
                data = self.recording_stream.read(recieveBytes)
                self.s.sendall(data)
            except:
                pass

client = Client()