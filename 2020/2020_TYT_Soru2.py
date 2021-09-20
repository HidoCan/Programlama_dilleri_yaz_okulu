import math
il=81
okul=16
mesaj=35
s1=il*okul*mesaj+il*okul
us=1
for k in range(okul):
    s2=pow(6,us)
    if s2==s1:
        break
    else:
        us+=1
print(s1,"=(6^6)")