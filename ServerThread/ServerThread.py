import socket
from threading import Thread

BUFFSIZE = 4096
SERVER_IP = "192.168.0.106"
SERVER_PORT = 1234

class ClientThread(Thread):
    def __init__(self,client_ip,client_port,conn):
        Thread.__init__(self)
        self.client_ip = client_ip
        self.client_port = client_port
        self.conn = conn
        print(f"New thread started for {client_ip}, {port}")

    def run(self):
        while True:
            try:
                data = self.conn.recv(BUFFSIZE)
            except:
                print("")
            print(f"Server received data: {data.decode()} from {self.client_ip}, {self.client_port}")
            if data.decode() == "exit":
                print("process killed")
                if listOfConnect != []:
                    for c in listOfConnect:
                        if self.conn != c:
                            c.close()
                if listOfThreads != []:
                    for t in listOfThreads:
                        if t.ident != self.ident:
                            t.join()
                break
            else:
                self.conn.send("RECEIVED".encode())

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
s.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
s.bind((SERVER_IP, SERVER_PORT))
s.listen(5)
listOfThreads = []
listOfConnect = []
print("Multithreaded Python server: Waiting for connection from TCP client")

while True:
    (conn, (ip,port)) = s.accept()
    newthread = ClientThread(ip,port,conn)
    newthread.start()
    listOfConnect.append(conn)
    listOfThreads.append(newthread)
