# Baska Bir Kod - Python Soru / Cevap

def faktoriyelHesapla(i):
    if i == 1:
        return 1

    else:
        return i * faktoriyelHesapla(i - 1)


def kombinasyonHesapla(j, k):
    if (j < k):
        print("1. Sayının 2. Sayıdan büyük yada eşit olması gerekli. Verdiğiniz sayıların çözümü yoktur!")

    elif (j == k):
        print("1")

    elif (j > k):

        s = 1
        s = faktoriyelHesapla(j)  # n faktöriyel

        l = 1
        l = faktoriyelHesapla(k)  # m faktöriyel

        f = 1
        f = faktoriyelHesapla(j - k)  # n-m faktöriyel

        w = s / (l * f)
        return w


print("Kombinasyon hesabı için lütfen sayıları giriniz.")

sayi1 = int(input("1. Sayı Giriniz: "))

sayi2 = int(input("2. Sayı Giriniz: "))

print("nSonuç:", kombinasyonHesapla(sayi1, sayi2))