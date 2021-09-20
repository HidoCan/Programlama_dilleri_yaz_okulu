

x = int(input("Alinan k kalem : "))
y = int(input("Alinan m kalem : "))
z = int(input("kalemlerin etiket fiyati : "))

k = 50/100
l = 30/100
z1 = z * k
z2 = z * l
m = z - z1
n = z - z2
a = x % 2

def hesapla(n,y,w):
    v = n * y
    q = w + v
    print("Toplam odenecek miktar : {0}".format(q))

if a == 0:
    p = x / 2
    r = p * z
    s = p * m
    w = r + s
    hesapla(n,y,w)
else :
    t = x - 1
    p = t / 2
    s = p * m
    r = p + 1
    w = r + s
    hesapla(n,y,w)