import socket
from threading import Thread

BUFFSIZE = 4096
SERVER_IP = "192.168.10.96"
SERVER_PORT = 1234

class ClientThread(Thread):
    def __init__(self,client_ip,client_port,conn):
        Thread.__init__(self)
        self.client_ip = client_ip
        self.client_port = client_port
        self.conn = conn
        print(f"New thread started for {client_ip}, {port}")

    def run(self):
        global kill
        while True:
            data = self.conn.recv(BUFFSIZE)
            print(f"Server received data: {data.decode()} from {self.client_ip}, {self.client_port}")
            if data.decode().lower == "exit":
                print("process killed")
                self.conn.send("exit".encode())
                for t in listOfThreads:
                    if Thread.get_ident() != t:
                        t.join()
                break
            self.conn.send("RECEIVED".encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_IP, SERVER_PORT))
s.listen(5)
listOfThreads = []
print("Multithreaded Python server: Waiting for connection from TCP client")

while True:
    (conn, (ip,port)) = s.accept()
    newthread = ClientThread(ip,port,conn)
    newthread.start()
    listOfThreads.append(newthread)
