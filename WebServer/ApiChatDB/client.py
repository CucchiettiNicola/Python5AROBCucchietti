import flask
from flask import request, jsonify
import sqlite3
import requests
from threading import Thread 
import time
import sys
import os

URL = "http://127.0.0.1:8080/api/v1/"
NumeroRegistro = 7                                 
db = "static/db_client_chat.db"        
stop_thread = False                         
class ReceiveThread(Thread):
    def __init__(self):
        Thread.__init__(self)
        self.connectionURL = URL + 'receive'
        self.PARAMS = {'IdDestinatario' : NumeroRegistro}

    def run(self):
        while True:
            if not stop_thread: 
                time.sleep(5)   
                r = requests.get(url = self.connectionURL, params=self.PARAMS)  
                data = r.json()
            
                try:
                    Sqlite = sqlite3.connect(db)
                    cursor = Sqlite.cursor()        
                    if len(data)!=0:
                        for d in data:
                            cursor.execute(f'''
                            SELECT bloccato
                            FROM utenti
                            WHERE user_id = {d[0]};''')
                            
                            if(not cursor.fetchall()[0][0]):
                                cursor.execute(f'''
                                INSERT INTO Messaggi(Text, IdMittente, IdDestinatario)
                                VALUES ("{d[3]}", {d[0]}), {d[1]};''')

                    Sqlite.commit()

                except sqlite3.Error as error:  
                    print("Error: " + error)

                finally:
                    if (Sqlite):
                        Sqlite.close()  
            else:
                break

def listaUtenti():
    try:
        Sqlite = sqlite3.connect(db)
        cursor = Sqlite.cursor()

        cursor.execute(f"SELECT * FROM utenti;")
        data = cursor.fetchall()
        for d in data:  
            print(f"ID: {d[0]} - Nome: {d[1]} - Cognome: {d[2]} - Bloccato: {3}")

    except sqlite3.Error as error:
        print("Error: " + error)

    finally:
        if (Sqlite):
            Sqlite.close()
    
def Ricevi():
    try:
        Sqlite = sqlite3.connect(db)
        cursor = Sqlite.cursor()

        cursor.execute(f"SELECT Messaggi.text, utenti.user_id FROM Messaggi, utenti WHERE utenti.user_id = Messaggi.IdDestinatario AND {numeroRegistro} = Messaggi.IdDestinatario;")
        data = cursor.fetchall()
        for d in data:
            print(f"Messaggio ricevuto da: {d[1]} - Testo: {d[0]}")
            
        Sqlite.commit()

    except sqlite3.Error as error:
        print("Error: " + error)

    finally:
        if (Sqlite):
            Sqlite.close()

def Manda():
    try:
        Sqlite = sqlite3.connect(db)
        cursor = Sqlite.cursor()

        idText = input('Numero di registro ricevente:\n>>>')

        cursor.execute(f"SELECT user_id FROM utenti WHERE user_id = '{idText}';")

        result = cursor.fetchall()
        if (len(result)==1):
            text = input('messaggio:\n>>>')
            PARAMS={'IdDestinatario':result[0][0], 'Text':text.replace(" ", "+"), 'IdMittente':NumeroRegistro}
            r = requests.get(url=URL+'send', params=PARAMS)
            if(r.status_code==200):
                cursor.execute(f"INSERT INTO Messaggi(Text, IdDestinatario, IdMittente) VALUES ('{text}', {result[0][0]}, {NumeroRegistro});")    
            else:
                print("Errore nell' invio")
        else:
            print("Errore nell'inserimento del numero di registro")
                
        Sqlite.commit()
            
    except sqlite3.Error as error:
        print("Error: " + error)

    finally:
        if (Sqlite):    #chiudo connessione
            Sqlite.close()

def bloccaSblocca():
    try:
        Sqlite = sqlite3.connect(db)
        cursor = Sqlite.cursor()

        idbloc = input("Numero registro persona bloccare/sbloccare:\n>>>")
        cursor.execute(f"SELECT bloccato FROM utenti WHERE user_id = {idbloc};")
        data = cursor.fetchall()
        if not data[0][0]:          
            print(f"Questo utente è bloccato. cambiare? (s/n))")
        else:
            print(f"Questo utente è sbloccato. cambiare? (s/n)")
    
        if(input().lower()=='s'):
            cursor.execute(f'''UPDATE utenti 
                                SET bloccato = {(data[0][0]+1)%2}
                                WHERE user_id = {idbloc}''')
            
        Sqlite.commit()

    except sqlite3.Error as error:
        print("Error: " + error)

    finally:
        if (Sqlite):
            Sqlite.close()

ReceaceThread = ReceiveThread()
ReceaceThread.start()
while True:
    k = int(input(f"""0 - Esci
    \n1 - Invia
    \n2 - Messaggi ricevuti
    \n3 - Rubrica
    \n4 - Blocca/Sblocca
    \n>>>"""))
    if k == 0:
        break
    elif k == 1:
        Manda()
    elif k == 2:
        Ricevi()        
    elif k == 3:
        listaUtenti()    
    elif k == 4:
        bloccaSblocca()

stop_thread = True
ReceaceThread.join()