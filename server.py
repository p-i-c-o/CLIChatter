import socket, os, time
from threading import Thread
from datetime import datetime

os.system('clear')

now = datetime.now()

nl = '''
'''

dt_string = now.strftime("%d/%m/%Y %H:%M:%S")
os.system(f'echo "{nl}" >> log.txt')
os.system(f'echo "{dt_string}" >> log.txt')

# server's IP address
SERVER_HOST = "" # Enter your SERVER IP ADDRESS
SERVER_PORT = 5002 # port we want to use
separator_token = "<SEP>" # we will use this to separate the client name & message


# initialize list/set of all connected client's sockets
client_sockets = set()
# create a TCP socket
s = socket.socket()
# make the port as reusable port
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
# bind the socket to the address we specified
s.bind((SERVER_HOST, SERVER_PORT))
# listen for upcoming connections
s.listen(10)
print(f"[*] Listening as {SERVER_HOST}:{SERVER_PORT}")

def listen_for_client(cs):
    """
    This function keep listening for a message from `cs` socket
    Whenever a message is received, broadcast it to all other connected clients
    """
    while True:
        try:
            # keep listening for a message from `cs` socket
            msg = cs.recv(1024).decode()
        except Exception as e:
            # client no longer connected
            # remove it from the set
            print(f"[!] Error: {e}")
            client_sockets.remove(cs)
        else:
            # if we received a message, replace the <SEP>
            # token with ": " for nice printing
            msg = msg.replace(separator_token, ": ")
            Fmsg = msg[5:]
            Fmsg = Fmsg[:-4]
            if Fmsg != '':
              os.system(f'echo "{Fmsg}" >> log.txt')
              print(msg)

        # iterate over all connected sockets
        for client_socket in client_sockets:
            # and send the message
            client_socket.send(msg.encode())


while True:
    # we keep listening for new connections all the time
    client_socket, client_address = s.accept()
    print(f"[+] {client_address} connected.")
    newcon = (f"[+] {client_address} connected.")
    os.system(f'echo "{newcon}" >> log.txt')
    # add the new connected client to connected sockets
    client_sockets.add(client_socket)
    # start a new thread that listens for each client's messages
    t = Thread(target=listen_for_client, args=(client_socket,))
    # make the thread daemon so it ends whenever the main thread ends
    t.daemon = True
    # start the thread
    t.start()

# close client sockets
for cs in client_sockets:
    cs.close()
# close server socket
s.close()

nl = '''
'''

os.system(f'echo "{nl}" >> log.txt')
