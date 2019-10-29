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

print(alfabetoLN)
print(alfabetoNL)

print(chiaveN)

parolaL = input("parola da crittografare\n>>>")
parolaN = []

for l in parolaL.upper():
    parolaN.append(alfabetoLN[l])

print(parolaN)
cnt = 0
#for nL in parolaN:
