

while True:
    a = int(input("Fotograf sayisi : "))
    b = int(input("Her birinin bulundugu : "))
    if b > a:
        continue
    else:
        k = b * 3
        a = a * 2
        x = k - a
        print("3'ünün birlikte bulundugu foto sayisi : {0}".format(x))
        break