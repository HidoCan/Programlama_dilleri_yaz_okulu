import math
a = input("Şu anki kasa fiyatı")
b = input("Kasada ödenen toplam para")
c = input("Kaç ürüne indirim uygulandı")
d = input("Ürün başına uygulanan indirim miktarı")
x = int(b) + (int(c)*int(d)) - int(a)
print(x)