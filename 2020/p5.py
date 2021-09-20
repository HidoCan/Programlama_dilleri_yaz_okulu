

k = int(input("Bina sayisi : "))
l = int(input("yikilan bina sayisi : "))
m = int(input("Kacti : "))
n = int(input("Kac oldu : "))

g = k * 3
x = g - m
y = k - x
p = n - m
l = l * 3
r = l - p
b = 100 / y
d = r * b

print("3 katli bina sayisinin azaldigi %{0}".format(d))