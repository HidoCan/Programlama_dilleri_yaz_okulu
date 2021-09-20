from math import factorial
n=int(input("C(n,r) kombinasyonu için n sayısını giriniz:"))
r=int(input("C(n,r) kombinasyonu için r sayısını giriniz:"))
kombinasyon=int(factorial(n)/(factorial(n-r)*factorial(r)))
print("C(",n,",",r,") =",kombinasyon)
