# imports
from http import server
import socket
import threading

# make sure you enter inactive ports
PORT = 5050
SERVER = "192.168.1.3" 
# equivalent to the above is
# SERVER = socket.gethostbyname(socket.gethostname()) 
# SERVER = "60.243.98.160"
ADDR = (SERVER, PORT)
# print(SERVER)
# The below 2 lines actually creates a socket and binds with this server
server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
server.bind(ADDR)
# How many bytes of data is received
HEADER = 64
# Formatig the recieved message to utf-8
FORMAT = "utf-8"

DISCONNECT_MSG = "!DISCONNECT"

# handles all request and repsonse of the client
def handle_client(conn, addr):
    print(f"[NEW CONNECTION] {addr} connected.")

    connected = True
    while connected:
        msg_length = conn.recv(HEADER).decode(FORMAT)
        if msg_length:
            msg_length = int(msg_length)
            msg = conn.recv(msg_length).decode(FORMAT)
            if msg == DISCONNECT_MSG:
                connected = False

            print(f"[{addr}] {msg}") 

    conn.close()

# this starts the function
def start():
    server.listen()
    print(f"[LISTENING] server is listening on {SERVER}")
    while True:
        conn, addr = server.accept()
        # creating a thread to handle clients (multithreading)
        thread = threading.Thread(target=handle_client, args=(conn, addr))
        thread.start()
        # printing the number fo active threads
        print(f"[ACTIVE CONNECTIONS] {threading.active_count() - 1}")


if __name__ == "__main__":
    print("[STARTING] server is starting....")
    start()
 