import socket, os
import random
from threading import Thread
from datetime import datetime
from colorama import Fore, init, Back


logo = """   █████╗ ██╗     ██╗     █████╗ ██╗  ██╗ █████╗ ████████╗████████╗███████╗██████╗
  ██╔══██╗██║     ██║    ██╔══██╗██║  ██║██╔══██╗╚══██╔══╝╚══██╔══╝██╔════╝██╔══██╗
  ██║  ╚═╝██║     ██║    ██║  ╚═╝███████║███████║   ██║      ██║   █████╗  ██████╔╝
  ██║  ██╗██║     ██║    ██║  ██╗██╔══██║██╔══██║   ██║      ██║   ██╔══╝  ██╔══██╗
  ╚█████╔╝███████╗██║    ╚█████╔╝██║  ██║██║  ██║   ██║      ██║   ███████╗██║  ██║
   ╚════╝ ╚══════╝╚═╝     ╚════╝ ╚═╝  ╚═╝╚═╝  ╚═╝   ╚═╝      ╚═╝   ╚══════╝╚═╝  ╚═╝"""

# init colors
init()

# set the available colors
colors = [Fore.BLUE, Fore.CYAN, Fore.GREEN, Fore.LIGHTBLACK_EX,
    Fore.LIGHTBLUE_EX, Fore.LIGHTCYAN_EX, Fore.LIGHTGREEN_EX,
    Fore.LIGHTMAGENTA_EX, Fore.LIGHTRED_EX, Fore.LIGHTWHITE_EX,
    Fore.LIGHTYELLOW_EX, Fore.MAGENTA, Fore.RED, Fore.WHITE, Fore.YELLOW
]

# choose a random color for the client
client_color = random.choice(colors)
os.system('clear')
print('\n')
print(logo + '\n')

print("To close this software, type 'exit' at any time!")

SERVER_HOST = input('Server IP address:    ')
if SERVER_HOST.lower() == 'exit':
  conf = input('Are you sure? [y/n]: ')
  if conf.lower() == 'y':
    exit()

while SERVER_HOST.isdigit() == False:
  SERVER_HOST = input('Thats not an IP address! Try Again:    ')
  if SERVER_HOST.lower() == 'exit':
    conf = input('Are you sure? [y/n]: ')
    if conf.lower() == 'y':
      exit()
# server's IP address
# if the server is not on this machine,
# put the private (network) IP address (e.g 192.168.1.2)
SERVER_PORT = 5002 # server's port
separator_token = "<SEP>" # we will use this to separate the client name & message

# initialize TCP socket
s = socket.socket()
print(f"[*] Connecting to {SERVER_HOST}:{SERVER_PORT}...")
# connect to the server
s.connect((SERVER_HOST, SERVER_PORT))
print("[+] Connected.")
# prompt the client for a name
name = input("Enter your name: ")
if name.lower() == 'exit':
  conf = input('Are you sure? [y/n]: ')
  if conf.lower() == 'y':
    exit()


def listen_for_messages():
    while True:
        message = s.recv(1024).decode()
        print(message)

# make a thread that listens for messages to this client & print them
t = Thread(target=listen_for_messages)
# make the thread daemon so it ends whenever the main thread ends
t.daemon = True
# start the thread
t.start()

while True:
    # input message we want to send to the server
    to_send =  input()
    if to_send.lower() == 'exit':
      conf = input('Are you sure? [y/n]: ')
      if conf.lower() == 'y':
        exit()
    print ("\033[A                             \033[A")

    # a way to exit the program
    if to_send.lower() == 'q':
        break
    # add the datetime, name & the color of the sender
    date_now = datetime.now().strftime('%Y-%m-%d %H:%M:%S')
    to_send = f"{client_color}[{date_now}] {name}{separator_token}{to_send}{Fore.RESET}"
    # finally, send the message
    s.send(to_send.encode())

# close the socket
s.close()
