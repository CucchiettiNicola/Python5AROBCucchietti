import socket as sck
from threading import Thread

BUFFSIZE = 4096
IP = '127.0.0.1'
PORT = 1234

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM) #ipv4 e tcpip
s.connect((IP, PORT))

while True:
    dataByte = s.recv(BUFFSIZE) #il client riceve l'operazione
    data = dataByte.decode() #decodifica
    if data == "exit": #terminazione client
        break
    else:
        risultato = eval(data) #esecuzione della operazione
        print(f'{data} = {risultato}') #print di conferma
        s.sendall((str(risultato)).encode()) #invio al server
s.close()
