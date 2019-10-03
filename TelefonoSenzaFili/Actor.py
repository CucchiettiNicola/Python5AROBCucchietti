import socket as sck
inizio = False
ultimo = False
HOST = "0.0.0.0"
SERVER = "192.168.10.56"
PORT = 8080
#s1: server
#s2: client
if not inizio:
    s1 = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
if not ultimo:
    s2 = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
if not inizio:
    s1.bind((HOST, PORT))
    s1.listen()
    conn, address = s1.accept()
    print("connesso")
while True:
    if not inizio:
        dataByte = conn.recv(4096)
        print("ricevuto stringa " + str(dataByte.decode()) + " da client " + str(address))
    else:
        stringa = input(">>> ")
    if not ultimo:
        s2.connect((SERVER, PORT))
        print("connesso")
        if inizio:
            s2.sendall(stringa.encode())
            if (stringa.lower() == "exit"):
                break
        else:
            s2.sendall(dataByte)
            if (str(dataByte.decode()).lower() == "exit"):
                break
        s2.close()
if not inizio:
    conn.close()
    s1.close()
if not ultimo:
    s2.close()
