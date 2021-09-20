
while True:
    x = int(input("Sifredeki rakam sayisi : "))
    if x > 9:
        continue
    elif x < 1:
        continue
    elif x > 5:
        print("Olasilik : 0")
        break
    else:
        a = 5 / 9
        b = 4 / 8
        c = 3 / 7
        d = 2 / 6
        e = 1 / 5

        if x == 1:
            print("Olasilik : {0}".format(a))
            break
        elif x == 2:
            print("Olasilik : {0}".format(a*b))
            break
        elif x == 3:
            print("Olasilik : {0}".format(a*b*c))
            break
        elif x == 4:
            print("Olasilik : {0}".format(a*b*c*d))
            break
        else:
            print("Olasilik : {0}".format(a*b*c*d*e))
            break

