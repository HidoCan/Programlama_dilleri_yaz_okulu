A={"0","1","4","5","6"}
B={"0","1","4","5","6"}
kesisim=A.intersection(B)
print ("A kesisim B :",set(kesisim))
fark = A.difference(B)

A_eleman_sayisi=9
B_eleman_sayisi=6
print ("A{} eleman sayısı:",A_eleman_sayisi)
print ("B{} eleman sayısı:",B_eleman_sayisi)
B.add("9")
A.update("2","3","7","8")
fark = A.difference(B)
print ("A=",fark)
A=[2,3,7,8]
toplam=sum(A)
print (toplam)