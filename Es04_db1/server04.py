import AlphaBot 
import socket
import RPi.GPIO as GPIO
import sqlite3

SERVER_ADD=("0.0.0.0",4000)
BUFFER=4096

DB="./db1_comandi.db"

def access_DB(db, key):
    con= sqlite3.connect(db)
    cur= con.cursor()
    
    res=cur.execute(f"SELECT command_description FROM movement WHERE key='{key}'")

    record=res.fetchall()
    print(record)

    command=record[0][0].split("|")   
    print(command)
    con.close()

    return command

access_DB(DB,"l")