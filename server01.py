import AlphaBot 
import socket
import time

SERVER_ADD=("0.0.0.0",4000)
BUFFER=4096
N=1 #num massimo

robot=AlphaBot.AlphaBot()
robot.stop()

diz_command={"forward":robot.forward, 
             "backward":robot.backward, 
             "left":robot.left, 
             "right":robot.right}

s=socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.bind(SERVER_ADD)

s.listen(N)

conn, address=s.accept()

while True:

    message=conn.recv(BUFFER).decode()

    comand,t= message.split("|")
    conn.send("Ricevuto".encode())

    diz_command[comand]()
    time.sleep(int(t))

    robot.stop()

    conn.send("Eseguito".encode())
    
    #conn.close()