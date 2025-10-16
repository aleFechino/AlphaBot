import socket
from pynput.keyboard import Key, Controller, Listener
import time

dictCommand={'w': 'forward-', 'a':'left-', 's': 'backward-', 'd':'right-'}


def on_press(key): #funzione che verrà chiamata quando un tasto qualunque viene premuto, salvando il tasto nel parametro key
    print(key)
    #print(type(key))
    s.send(dictCommand[key.char].encode())
    

def on_release(key):
    s.send('stop-'.encode())
        

listener = Listener(on_press=on_press, on_release=on_release)# creo istanza di listen che permette di mandare le funzioni on_press e on_release
listener.start()  # attivo in backgrund l'ascolto dei tasti premuti

#ho sempre una lista che contiene i tasti che sto premento, analizzando quella lista posso capire cosa mandare al server, nel caso la lista sia vuota mando stop

SERVER_ADD=("192.168.208.1",4000)  #.1.123
BUFFER=4096

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(SERVER_ADD)

while True:
    pass



    #print(keyPressed)
    #if len(keyPressed)==0:  #lista vuota mando stop
        #s.send('stop|'.encode())
        #currentCommand='stop-'

    #else:
    #    for i in range(len(keyPressed)):
            #s.send(f'{keyPressed[i]}|'.encode())
    #        currentCommand=dictCommand[keyPressed[i]]

    # if currentCommand != previousCommand:
    #     s.send(currentCommand.encode())
    #     previousCommand=currentCommand
        
    


    

    