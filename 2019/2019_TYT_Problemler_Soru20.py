a = input("Yağ şişelerinin kapasitesi")
b = input("Kaç adet argan yağı kullanılacak")
c = input("Kaç adet zeytinyağı kullanılacak")
d = input("Kaç mililitrede bir yumurta eklenecek")
a = int(a)
b = int(b)
c = int(c)
d = int(d)

x = 100*a*b/40
v = x+(a*b)
t = v/d
h = 100*a*c/75
j = h+a*c
k = j/d
s = t+k
print (s)
