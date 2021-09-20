# Baska Bir Kod - Python Soru / Cevap
sayi = int(input("Sayi Giriniz:"))

toplam = 0

for i in range(1, sayi):
    print(i)
    if (sayi % i == 0):
        toplam += i

if (sayi == toplam):
    print("Mükemmel Sayidir.")
else:
    print("Mükemmel Sayi Degildir")