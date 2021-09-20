
a = int(input("Mevcut Sicaklik : "))

while True:
    b = int(input("Tahmin Degeri 1: "))
    c = int(input("Tahmin Degeri 2 : "))

    if b >= c:
        continue
    else:
       min = a + b
       max = a + c
       print("Sicakligin alabilecegi min deger : ",min)
       print("Sicakligin alabilecegi max deger : ",max)
       break
