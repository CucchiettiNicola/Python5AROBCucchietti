alfabetoNL = {
    0: "A",
    1: "B",
    2: "C",
    3: "D",
    4: "E",
    5: "F",
    6: "G",
    7: "H",
    8: "I",
    9: "L",
    10: "M",
    11: "N",
    12: "O",
    13: "P",
    14: "Q",
    15: "R",
    16: "S",
    17: "T",
    18: "U",
    19: "V",
    20: "Z"
}

alfabetoLN = {}

for n,l in alfabetoNL.items():
    alfabetoLN[l] = n

chiaveL = "ItisDelpozzo"
chiaveN = []

for l in chiaveL.upper():
    chiaveN.append(alfabetoLN[l])

print(chiaveL + "\n" + str(chiaveN))
while True:
    codificaDecodifica = input("0: Codifica\n1: Decodifica\n>>>")
    if codificaDecodifica == "0":
        parolaL = chiaveL + " "
        while len(chiaveL) <= len(parolaL):
            parolaL = input("\nparola da crittografare\n>>>")
            if len(chiaveL) <= len(parolaL):
                print("\nerrore: parola più lunga della chiave\n")
        parolaN = []

        for l in parolaL.upper():
            parolaN.append(alfabetoLN[l])

        parolaCritN = []

        for k in range(0, len(parolaN)):
            parolaCritN.append((parolaN[k] + chiaveN[k]) % 21)

        parolaCritL = ""

        for n in parolaCritN:
            parolaCritL = parolaCritL + alfabetoNL[n]

        print(parolaCritL)

    else:

        parolaCritL = chiaveL + " "
        while len(chiaveL) <= len(parolaCritL):
            parolaCritL = input("\nparola da Decrittografare\n>>>")
            if len(chiaveL) <= len(parolaCritL):
                print("\nerrore: parola più lunga della chiave\n")
        parolaCritN = []

        for l in parolaCritL.upper():
            parolaCritN.append(alfabetoLN[l])

        parolaN = []

        for k in range(0, len(parolaCritN)):
            parolaN.append((parolaCritN[k] - chiaveN[k]) % 21)

        parolaL = ""

        for n in parolaN:
            parolaL = parolaL + alfabetoNL[n]

        print(parolaL)
