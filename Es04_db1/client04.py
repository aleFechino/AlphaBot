import socket
import time 
from pynput.keyboard import Key, Controller, Listener

pressed=set()   #crea un insieme di elementi senza inserire i duplicati

def on_press(key): #funzione che verrà chiamata quando un tasto qualunque viene premuto, salvando il tasto nel parametro key
    #time.sleep(0.1)
    if key.char not in pressed:
        pressed.add(key.char)
        print(key)
        s.send(f'{key.char}-'.encode())

def on_release(key):
    if key.char in pressed:
        pressed.remove(key.char)
        s.send('stop-'.encode())

listener = Listener(on_press=on_press, on_release=on_release)# creo istanza di listen che permette di mandare le funzioni on_press e on_release
listener.start()  # attivo in backgrund l'ascolto dei tasti premuti

#ho sempre una lista che contiene i tasti che sto premento, analizzando quella lista posso capire cosa mandare al server, nel caso la lista sia vuota mando stop

SERVER_ADD=("192.168.1.123",4000)  #.1.123
BUFFER=4096

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(SERVER_ADD)

while True:
    pass