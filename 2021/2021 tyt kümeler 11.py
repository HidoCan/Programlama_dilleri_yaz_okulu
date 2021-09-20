A={"a"}
print ("asker")
print("ressam")
print("akademisyen")
Aelemansayisi=9
print ("A{} eleman sayısı:",Aelemansayisi)
A.update("a","s","k","e","r","m")
print (A)
şıklar=input("Şıkları giriniz:")
A.update (şıklar)
print (A)
if (len(A)>9):
	print ("Eleman sayısını aştı girilen şık:",şıklar)