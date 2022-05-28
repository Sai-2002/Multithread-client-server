# imports
from http import client
import socket

# Variables
PORT = 5050
SERVER = "60.243.98.160"
HEADER = 64
# Formatig the recieved message to utf-8
FORMAT = "utf-8"
DISCONNECT_MSG = "!DISCONNECT"
ADDR = (SERVER, PORT)

client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client.connect(ADDR)

def send(msg):
    message = msg.encode(FORMAT)
    msg_length = len(message)
    send_length = str(msg_length).encode(FORMAT)
    send_length += b' ' * (HEADER - len(send_length))
    client.send(send_length)
    client.send(message)

if __name__ == "__main__":
    send("Connection successful")
