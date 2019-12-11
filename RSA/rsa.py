import math

#p
p = int(input("inserire P\n>>>"))

#q
q = int(input("inserire Q\n>>>"))

#n
n = int(p * q)
print(f"n = {n}")

#m
m = 0
if p>=q:
    mag = p
else:
    mag = q
while m==0:
    if (mag % (p-1) == 0) and (mag % (q-1) == 0):
        m = mag
        break
    mag = mag + 1
print(f"m = {m}") 

#c
while(True):
    c = int(input("1<c<m c:\n>>>"))
    if math.gcd(c, m)==1:
        break

#d
d = 0
while(True):
    if (c*d)%m == 1:
        break
    else:
        d = d + 1

print(f"d = {d}")

print(f"Chiave pubblica: n = {n}, c = {c} \nChiave privata: m = {m}, d = {d}")