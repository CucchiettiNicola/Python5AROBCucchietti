import socket as sck

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.connect(('192.168.0.96', 1234))
print("connesso")
while True:
    stringaDaInviare = input()
    s.sendall(stringaDaInviare.encode())
    if stringaDaInviare == "exit":
        break
    dataByte = s.recv(4096)
    if dataByte.decode() == "exit":
        break
    print(dataByte.decode())
s.close()
