
sayi=input("Bir sayı girin: ")
carpim=1
for rakam in str(sayi):
  if int(rakam) != 0:
    carpim *= int(rakam)
print("sayının rakamları çarpımı:",carpim)