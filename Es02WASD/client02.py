import socket
from pynput.keyboard import Key, Controller, Listener

dictCommand={"'w'": 'forward-', "'a'":'left-', "'s'": 'backward-', "'d'":'right-'}

keyPressed=[] #lista che contiene tutti i tasti che sono premuti in un istante di tempo.

def on_press(key): #funzione che verrà chiamata quando un tasto qualunque viene premuto, salvando il tasto nel parametro key
    #print(f'"{key}"')
    if f'"{key}"' not in keyPressed:   #se premo un tasto lo aggiungo ad una lista nel caso esso non sia già nella lista
        keyPressed.append(str(key))

def on_release(key):
    try:
        keyPressed.remove(key)  # quando rilascio il tasto lo rimuovo dalla lista
    except ValueError:
        pass

listener = Listener(on_press=on_press, on_release=on_release)# creo istanza di listen che permette di mandare le funzioni on_press e on_release
listener.start()  # attivo in backgrund l'ascolto dei tasti premuti

#ho sempre una lista che contiene i tasti che sto premento, analizzando quella lista posso capire cosa mandare al serve, nel caso la lista sia vuota mando stop

SERVER_ADD=("192.168.1.19",4000)
BUFFER=4096

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)

s.connect(SERVER_ADD)

previousCommand='stop-'
while True:
    print(keyPressed)
    if len(keyPressed)==0:  #lista vuota mando stop
        #s.send('stop|'.encode())
        currentCommand='stop-'

    else:
        for i in range(len(keyPressed)):
            #s.send(f'{keyPressed[i]}|'.encode())
            currentCommand=dictCommand[keyPressed[i]]

    if currentCommand != previousCommand:
        s.send(currentCommand.encode())
        previousCommand=currentCommand
        
    


    

    