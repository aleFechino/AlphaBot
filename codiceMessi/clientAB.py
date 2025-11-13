import socket
import time
from pynput import keyboard

SERVER_ADRS = ("192.168.1.115", 8080)
BUFFER = 4096

# Creo un socket IPv4 TCP
s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.connect(SERVER_ADRS)

# Provo a ricevere un messaggio iniziale dal server, ma senza bloccare
s.settimeout(2)
try:
    data = s.recv(BUFFER)
    if data:
        print("Server dice:", data.decode())
except socket.timeout:
    print("---------- SCRIVI I COMANDI ----------")

def on_press(key):
    try:
        if key.char == 'w':
            print("Avanti")
            s.sendall(b"avanti")
            
        elif key.char == 's':
            print("Indietro")
            s.sendall(b"indietro")
            
        elif key.char == 'a':
            print("Sinistra")
            s.sendall(b"sinistra")
            
        elif key.char == 'd':
            print("Destra")
            s.sendall(b"destra")
        
        elif key.char == 'f': # serve per sbuggarlo
            print("Stop")
            s.sendall(b"stop")

        elif key.char == 'q': # comando dal bd per fare un quadrato
            print("Quadrato")
            s.sendall(b"quadrato")
        
        elif key.char == 'e': # comando dal bd per fare avanti e indietro 
            print("Avanti_Indietro")
            s.sendall(b"avanti_indietro")

    except AttributeError:
        pass

def on_release(key):
    try:
        if key.char in ['w', 'a', 's', 'd']:
            print("Stop")
            s.sendall(b"stop")
            
    except AttributeError:
        pass

# Avvio il listener UNA volta
with keyboard.Listener(on_press=on_press, on_release=on_release) as listener:
    listener.join()
