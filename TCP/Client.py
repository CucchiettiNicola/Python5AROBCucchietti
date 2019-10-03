import socket as sck

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.connect(('192.168.10.61', 65432))
print("connesso")
while True:
    stringaDaInviare = input()
    s.sendall(stringaDaInviare.encode())
    if stringaDaInviare == "0":
        break
    dataByte = s.recv(4096)
    if dataByte.decode() == "0":
        break
    print(dataByte.decode())
s.close()
