import socket
from threading import Thread

BUFFSIZE = 4096
SERVER_IP = "127.0.0.1"
SERVER_PORT = 1234

class ClientThread(Thread):
    def __init__(self,client_ip,client_port):
        Thread.__init__(self)
        self.client_ip = client_ip
        self.client_port = client_port
        print (f"New thread started for {client_ip}, {port}")

    def run(self):
        while True:
            data = conn.recv(BUFFSIZE)
            print(f"Server received data: {data.decode()} from {self.client_ip}, {self.client_port}")
            if data.decode() == "exit":
                break
            conn.send("RECEIVED".encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_IP, SERVER_PORT))
s.listen(5)
listOfTherads = []
print("Multithreaded Python server: Waiting for connection from TCP client")

while True:
    (conn, (ip,port)) = s.accept()
    newthread = ClientThread(ip,port)
    newthread.start()
    listOfTherads.append(newthread)

for t in listOfThreads:
    t.join()
