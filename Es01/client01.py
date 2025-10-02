import socket
import time

SERVER_ADD=("192.168.1.123",4000)
BUFFER=4096


s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(SERVER_ADD)

while True:

    message=input("Inserisci comando e tempo: ")
    _, t=message.split("|")

    s.send(message.encode())

    mesRecv=s.recv(BUFFER).decode()
    print(f"Messaggio ricevuto: {mesRecv}")
    mesRecv=s.recv(BUFFER).decode()
    print(f"Messaggio ricevuto: {mesRecv}")
