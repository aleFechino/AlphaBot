#import AlphaBot 
import socket
import time

SERVER_ADD=("0.0.0.0",4000)
BUFFER=4096
N=1 #num massimo

#robot=AlphaBot.AlphaBot()
robot=AlphaBot()
robot.stop()

diz_command={"forward":robot.forward, 
             "backward":robot.backward, 
             "left":robot.left, 
             "right":robot.right,
             "stop":robot.stop}

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(SERVER_ADD)

s.listen(N)

conn, address=s.accept()
try: 
    while True:     #nel while true ora leggo solo il messaggio e stampo la funzione di conseguenza.
        
        message=conn.recv(BUFFER).decode()
        #print(message)
        listCommand=message.split('-')
        #print(listCommand)
        #for cmd in listCommand:
        diz_command[listCommand[len(listCommand)-2]]()

except KeyboardInterrupt:
    print('interrotto')
