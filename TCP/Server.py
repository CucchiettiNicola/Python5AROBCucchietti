import socket as sck

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.bind(('0.0.0.0', 65432))
s.listen()

conn, address = s.accept()
print("connesso")
while True:
    dataByte = conn.recv(4096)
    print(dataByte.decode())
    if dataByte.decode() == "0":
        break
    stringaDaInviare = input()
    conn.sendall(stringaDaInviare.encode())
    if stringaDaInviare == "0":
        break
conn.close()
s.close()
