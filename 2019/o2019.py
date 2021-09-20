

while True:
    a = int(input("1.sayi : "))
    b = int(input("2.sayi : "))
    c = int(input("3.sayi : "))
    d = int(input("4.sayi : "))
    k = a + 2
    l = b + 2
    m = c + 2
    if k == b:
        if l == c:
            if m == d:
                x = b + c
                print("yas : {0}".format(x))
                break
            else:
                continue
        else:
            continue
    else:
        continue