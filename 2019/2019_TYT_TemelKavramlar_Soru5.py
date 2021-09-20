from math import *
a = input("Kenar sayısı")
b = input("İçerdiği sayı")
c = input ("Küçük kenar sayısı")
d = input("Büyük kenar sayısı")
a = int(a)
b = int(b)
c = int(c)
d = int(d)

x = a/b
x = floor(x)

f = x * c
e = x * d

while e/c > x+1:
    e = e+1
    break
while f/d < x:
    f = f+1
    break
if e==f:
    toplam = 0
    for rakam in e:
        toplam += int(rakam)

    print("sayının rakamları toplamı:", toplam)
else:
    print("e ve f dahil arasındaki bütün sayıları al"
          "herbirinin basamaklarını ayrı ayrı topla"
          "topladğıgın basamakların sonuçlarından birbirinden farklı olanları yazdır")