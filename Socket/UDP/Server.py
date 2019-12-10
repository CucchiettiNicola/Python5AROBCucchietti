import socket as sck

s = sck.socket(sck.AF_INET, sck.SOCK_DGRAM)
s.bind(('0.0.0.0', 54321))

while True:
    data, address = s.recvfrom(4096)
    print(data.decode() + "da" + str(address))
    s.sendto(data, address)
    if data.decode() == "":
        break
s.close()
