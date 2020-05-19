import flask
from flask import request, jsonify
import sqlite3
from datetime import datetime
import os

app = flask.Flask(__name__)
db = 'static/db_server_chat.db'

@app.route('/api/v1/receive', methods=['GET'])
def Testo():     
    if (flask.request.method == 'GET'):
        if 'IdDestinatario' in request.args:   
            Destinatario = int(request.args['IdDestinatario'])
        try:
            Sqlite = sqlite3.connect(db)
            cursor = Sqlite.cursor()

            cursor.execute(f"SELECT IdMittente,text,IdDestinatario,timestamp FROM Messaggi AND IdDestinatario = {Destinatario}")
            Messaggi = cursor.fetchall()

            if len(Messaggi) != 0:
                Sqlite.commit()
            else:
                return []

        except sqlite3.Error as error:
            print("Error: " + error)

        finally:
            if (Sqlite):
                print('Chiusura connessione DB')
                Sqlite.close()
                return jsonify(Messaggi)

@app.route('/api/v1/send', methods=['GET', 'POST'])
def apiInvio():
    if request.method == 'GET':
        if 'IdDestinatario' in request.args and 'text' in request.args and 'idMittente' in request.args:
            Destinatario = int(request.args['IdDestinatario'])
            text = request.args['text']
            Mittente = int(request.args['IdMittente'])
        else:
            return 'Error missing arguments'
        
        try:
            Sqlite = sqlite3.connect(db)
            cursor = Sqlite.cursor()
            
            cursor.execute(f'''SELECT user_id
                                FROM utenti
                                WHERE user_id = {Destinatario} or user_id = {Mittente};''')

            user = cursor.fetchall()

            if (len(user)>1):
                date = datetime.now() 
                time = date.strftime("%H:%M:%S")

                cursor.execute(f'''
                    INSERT INTO messaggi(IdDestinatario, IdMittente, text, timestamp) 
                    VALUES ({Destinatario}, {Mittente}, "{text}", "{time}";''')

                Sqlite.commit()
            else:
                return 'Utenti non registrati'

        except sqlite3.Error as error:
            print('Error: ' + error)
        
        finally:
            if (Sqlite):
                Sqlite.close()
                return 'Messaggio inviato'

if __name__== "__main__": 
    app.run(host="0.0.0.0", port=int(8080), debug=True)