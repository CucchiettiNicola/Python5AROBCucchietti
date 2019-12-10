import socket as sck
from threading import Thread

NickName = "Cucchietti"

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.connect(('192.168.0.102', 2500))
print("connesso")

class Receive(Thread):
    def __init__(self, s):
        Thread.__init__(self)
        self.s = s
        print(f"Ricevo")

    def run(self):
        print("partito receive")
        while True:
            data = self.s.recv(4096)
            dataSplit = (data.decode()).split('§')
            print("\n" + dataSplit[1] + ": " + dataSplit[2])
            if dataSplit[2] == "exit":
                break
        self.s.close()

class Send(Thread):
    def __init__(self, s):
        Thread.__init__(self)
        self.s = s
        print(f"Mando")

    def run(self):
        print("partito send")
        while True:
            destinatario = input("destinatario\n>>>\n")
            stringaDaInviare = input("messaggio\n>>>\n")
            s.sendall((destinatario + "§" + NickName + "§" + stringaDaInviare).encode())
            if stringaDaInviare == "exit":
                break
        self.s.close()

receive = Receive(s)
send = Send(s)
receive.start()
send.start()
