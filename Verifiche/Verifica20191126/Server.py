import socket as skt
from threading import Thread
import sqlite3

BUFFSIZE = 4096
SERVER_IP = "127.0.0.1"
SERVER_PORT = 1234

class ClientThread(Thread):
    def __init__(self, client_ip, client_port, conn, contatore): #metodo eseguito alla crazione del thread
        Thread.__init__(self)
        self.ip = client_ip
        self.port = client_port
        self.conn = conn
        self.numeroClient = contatore


    def run(self): #metodo che si utilizza all' esecuzione del thread
        for op in operazioni: #cicla affinche non ci sono più operazioni
            if op[0] == self.numeroClient: #verifico se deve fare l'operazione
                self.conn.send(op[1].encode()) #invio l'operazione
                print(f'{op[1]} = {(self.conn.recv(BUFFSIZE)).decode()} from {self.ip} - {self.port}') #ricevo l'operazione e stampo su terminale
        self.conn.send("exit".encode()) #quando finito esco


s = skt.socket(skt.AF_INET, skt.SOCK_STREAM) #ipv4 e tcpip
s.setsockopt(skt.SOL_SOCKET, skt.SO_REUSEADDR, 1) #il socket riutilizza le porte
s.bind((SERVER_IP, SERVER_PORT)) #associo l'ip alla porta per permettere la connessione del client
s.listen(5) #il server accetterà al massimo 5 connessioni alla volta
contatore = 0 #variabile per identificare il numero del client che si connette

#-----------creazione di una lista delle operazione con il client associato-------
operazioni = []
db = sqlite3.connect('operations.db') #connetto al database
c = db.cursor() #creo un puntatore
for row in c.execute(f'SELECT * FROM operations'): #faccio una query
    (dbid, client, operation) = row
    operazioni.append([int(client), str(operation)]) # e creo la lista
c.close() #chiudo puntatore
db.close() #chiudo il database
#-------------------------------------------------------
while True:
    (conn, (ip, port)) = s.accept() #accettazione della connessione
    contatore = contatore + 1
    newthread = ClientThread(ip, port, conn, contatore) #creazione della classe del thread
    newthread.start() #avvio del thread
