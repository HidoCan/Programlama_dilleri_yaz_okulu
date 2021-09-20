

a = float(input("Cayin fiyati : "))
b = float(input("Portakal suyunun fiyati : "))
x = float(input("Icilen cay : "))
y = float(input("Icilen portakal suyu : "))

c = a * x
p = b * y
s = p * c
w = 2/7
v = s * w

print("Tatlinin fiyati : {0}".format(v))