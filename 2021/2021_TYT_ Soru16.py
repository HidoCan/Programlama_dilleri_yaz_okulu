print("Python 2 Bilinmeyenli Denklem Kökü Bulma Programı")
print("Denkleminiz 2. dereceden yani (ax**2+b*x+c) şeklinde olmak zorundadır.")
a=int(input("A sayısını giriniz:"))
b=int(input("B sayısını giriniz:"))
c=int(input("C sayısını giriniz:"))
delta=b**2-4*a*c
x1 = (-b - delta ** 0.5)/ (2 * a)
x2 = (-b + delta ** 0.5) / (2 * a)
if delta<0:
    print("Reel kök yoktur.")
if delta==0:
    print("Çakışık 2 kök vardır.")
print("Denkleminizin birinci kökü:{}\n Denkleminizin ikinci kökü:{}\n".format(x1,x2))
if delta>0:
    print("Gerçek 2 kök vardır.")
    print("Denkleminizin birinci kökü:{}\n Denkleminizin ikinci kökü:{}\n".format(x1,x2))
