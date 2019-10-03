import socket as sck
s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)

while True:
    testo = input(">>>")
    s.sendto(testo.encode(), ("127.0.0.1", 8080))
    if (testo == ""):
        break
    data, server = s.recvfrom(4096)
    print(data.decode())
s.close()