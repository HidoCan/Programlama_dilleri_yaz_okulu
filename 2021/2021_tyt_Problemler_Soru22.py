pizza=int(input("Birinci ürün fiyatını Giriniz:"))
pizza1 =int(input("İkinci ürün fiyatını Giriniz:"))
 
toplam=pizza+pizza1
 
if(toplam<9):
    print("Ödenecek miktar:",toplam)
else:
    indirim=toplam-(toplam*0.15)
    toplam=toplam-indirim
    print("İndirim miktarı:",indirim)
    print("Ödenecek miktar:",toplam)
