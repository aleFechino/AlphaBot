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
import time
import RPi.GPIO as GPIO
import sqlite3

SERVER_ADD=("0.0.0.0",4001)
BUFFER=1024
N=1
DB="./db1_comandi.db"



def access_DB(db, key):
    con= sqlite3.connect(db)
    cur= con.cursor()
    
    res=cur.execute(f"SELECT command_description FROM movement WHERE key='{key}'")

    record=res.fetchall()
    #print(record)

    commands=record[0][0].split("|")
    #print(command)
    con.close()

    return commands


def run_db(comands):
    for com in comands:
        move=com.split(",")
        print(move)
        diz_command[move[0]]()
        time.sleep(int(move[1]))

robot=AlphaBot.AlphaBot()
#robot=AlphaBot()
robot.stop()
diz_command_wasd={'w':"forward",
                  's': "backward",
                  'a':"left",
                  'd':"right",
                  'stop':"stop"}

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
        listCommand=message.split('-')
        key = listCommand[-2]
        if key in diz_command_wasd:    
            #print(f'dentro if {key}')    
             com = diz_command_wasd[key]
             diz_command[com]()
        else:
            #print(f'fuori if {key}')    
             comands = access_DB(DB, key)
             run_db(comands)
except KeyboardInterrupt:
    print('interrotto')
