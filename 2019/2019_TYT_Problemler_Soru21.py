a = input("tahta kasa sayısı")
b = input("plastik kasa sayısı")
c = input("sadece tahta kasalarla dolum oranı")
d = input("sadece plastik kasalarla dolum oranı")
f = input("dolu bir tahta kasadaki domates kilosu")
a = int(a)
b = int(b)
c = int(c)
d = int(d)
f = int(f)
q = a*f
x = q/c
y = x*d/b
print(y)