import socket as sck

NickName = "Nicola"

s = sck.socket(sck.AF_INET, sck.SOCK_STREAM)
s.connect(('192.168.10.72', 1234))
print("connesso")

mod = int(input("1 per inviare prima\n2 per ricevere prima\n>>>"))

while True:
    if mod == 1:
        destinatario = input("destinatario\n>>>")
        stringaDaInviare = input("messaggio\n>>>")
        s.sendall((destinatario + "§" + NickName + "§" + stringaDaInviare).encode())
        if stringaDaInviare == "exit":
            break
        else:
            data = s.recv(4096)
            dataSplit = (data.decode()).split('§')
            print(dataSplit[1] + ": " + dataSplit[2])
            if dataSplit[2] == "exit":
                break
    else:
        data = s.recv(4096)
        dataSplit = (data.decode()).split('§')
        print(dataSplit[1] + ": " + dataSplit[2])
        if dataSplit[2] == "exit":
            break
        else:
            destinatario = input("destinatario\n>>>")
            stringaDaInviare = input("messaggio\n>>>")
            s.sendall((destinatario + "§" + NickName + "§" + stringaDaInviare).encode())
            if stringaDaInviare == "exit":
                break

s.close()
