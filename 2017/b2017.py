
while True:
    a = int(input("birinci sayı : "))
    b = int(input("ikinci sayı : "))
    z = b - 1

    if a >= z:
        continue
    else:
        t = 0
        while True:
            t = z + t
            z = z - 1
            if z == a:
                print("Sonuc : ",t)
                break
            else :
                continue
        break
