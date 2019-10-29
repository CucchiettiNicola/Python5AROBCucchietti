import socket as skt
from threading import Thread
import sqlite3

BUFFSIZE = 4096
SERVER_IP = "0.0.0.0"
SERVER_PORT = 1234


class ClientThread(Thread):
    def __init__(self, client_ip, client_port, conn):
        Thread.__init__(self)
        self.client_ip = client_ip
        self.client_port = client_port
        self.conn = conn
        print(f"New thread started for {client_ip}, {port}")

    def run(self):
        while True:
            #try:
                data = self.conn.recv(BUFFSIZE)
                dataSplit = (data.decode()).split('§')

                destinatario = dataSplit[0]
                mittente = dataSplit[1]
                testo = dataSplit[2]

                db = sqlite3.connect('prova.db')
                c = db.cursor()

                for row in c.execute(f'SELECT * FROM CLIENT WHERE nick_name = "{destinatario}"'):
                    (id, nick_name, dbip, dbport) = row

                connDestinatario = DcOfConnect[dbip]

                if testo == 'exit':
                    connDestinatario.send((destinatario + "§" + mittente + "§" + "exit").encode())
                    break
                else:
                    connDestinatario.send((destinatario + "§" + mittente + "§" + testo).encode())

            #except:
            #    print("errore: Uscita dal programma")
            #    break


s = skt.socket(skt.AF_INET, skt.SOCK_STREAM)
s.setsockopt(skt.SOL_SOCKET, skt.SO_REUSEADDR, 1)
s.bind((SERVER_IP, SERVER_PORT))
s.listen(5)
listOfThreads = []
DcOfConnect = {}

while True:
    (conn, (ip, port)) = s.accept()
    newthread = ClientThread(ip, port, conn)
    newthread.start()
    DcOfConnect[ip] = conn
    listOfThreads.append(newthread)
