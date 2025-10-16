# class AlphaBot:                 #creo una classe alphabot di test che ha stesse funzioni di AlphaBot originale, ma stampa solo su terminale nome funzione.
#     def __init__(self):
#         self.v=0

#     def forward(self):
#         print('forward')
    
#     def backward(self):
#         print('backward')

#     def left(self):
#       print('left')

#     def right(self):
#         print('right')

#     def stop(self):
#         print('stop')

import AlphaBot 
import socket
import RPi.GPIO as GPIO

SERVER_ADD=("0.0.0.0",4000)
BUFFER=4096
N=1 #num massimo

DR=16 #sensore destro
DL=19 #sensore sinistro

def funzione_sensori():
    print("entrato")
    #setto le resistenze in pull up
    GPIO.setup(DR, GPIO.IN, GPIO.PUD_UP)
    GPIO.setup(DL, GPIO.IN, GPIO.PUD_UP)

    while True:
        DR_status= GPIO.input(DR)
        DL_status= GPIO.input(DL)

        if(DR_status==0):
            print("rilevato destro")

        if(DL_status==0):
            print("rilevato sinistro")


#robot=AlphaBot.AlphaBot()
robot=AlphaBot()
robot.stop()
funzione_sensori()

# diz_command={"forward":robot.forward, 
#              "backward":robot.backward, 
#              "left":robot.left, 
#              "right":robot.right,
#              "stop":robot.stop}

# s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
# s.bind(SERVER_ADD)

# s.listen(N)

# conn, address=s.accept()
# funzione_sensori()

# try: 
#     while True:     #nel while true ora leggo solo il messaggio e stampo la funzione di conseguenza.
        
#         message=conn.recv(BUFFER).decode()
#         #print(message)
#         listCommand=message.split('-')
#         #print(listCommand)
#         #for cmd in listCommand:
#         diz_command[listCommand[len(listCommand)-2]]()

# except KeyboardInterrupt:
#     print('interrotto')
