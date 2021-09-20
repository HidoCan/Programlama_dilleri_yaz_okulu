

ab = int(input("Ardanin berki ebeleme ihtimali % : "))
ac = int(input("Ardanin cani ebeleme ihtimali % : "))
ba = int(input("Berkinin ardayi ebeleme ihtimali % : "))
bc = int(input("Berkinin cani ebeleme ihtimali % : "))
ca = int(input("Canin ardayi ebeleme ihtimali % : "))
cb = int(input("Canin berki ebeleme ihtimali % : "))

while True:
    ie = input("Ilk ebe kim : ")
    x = ab / 100
    y = ac / 100
    z = ba / 100
    k = bc / 100
    l = ca / 100
    m = cb / 100

    arda = "arda"
    berke = "berke"
    can = "can"

    if ie == arda:
        p = z * x
        r = y * l
        s = p + r
        w = s * 100
        print("3 ebenin tekrar {0} olma olasiligi : %{1}".format(ie, w))
    elif ie == berke:
        p = z * x
        r = k * m
        s = p + r
        w = s * 100
        print("3 ebenin tekrar {0} olma olasiligi : %{1}".format(ie, w))
    elif ie == can:
        p = k * m
        r = y * l
        s = p + r
        w = s * 100
        print("3 ebenin tekrar {0} olma olasiligi : %{1}".format(ie, w))
    else:
        break