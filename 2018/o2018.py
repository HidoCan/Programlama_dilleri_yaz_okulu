
while True:
    a = int(input("Ilk kilo : "))
    b = int(input("Ikinci kilo : "))
    k = a+1

    if k == b:
        while True:
            x = int(input("1 kilogram fazla tartma olasiligi : "))
            y = int(input("1 kilogram az tartma olasiligi : "))
            z = x + y

            if z >= 100:
                continue
            else:
                w = 100 - z
                p = w * y
                r = x * w
                s = p + r
                v = s / 100
                print("Kiloların esit cikma olasiligi %{0}".format(v))
                break
    else:
        continue