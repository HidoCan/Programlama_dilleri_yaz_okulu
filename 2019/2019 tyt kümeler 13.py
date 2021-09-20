A={""}
B={""}
C={""}

sayi= input("Sayı giriniz: ")
sayi=int(sayi)
if (sayi%2==0):
	A.add(sayi)

if (sayi%3==0):
	B.add(sayi)
if (sayi%12==0):
	C.add(sayi)
sayi= input("Sayı giriniz: ")

sayi=int(sayi)
if (sayi%2==0):
	A.add(sayi)

if (sayi%3==0):
	B.add(sayi)
if (sayi%12==0):
	C.add(sayi)
sayi= input("Sayı giriniz: ")
sayi=int(sayi)
if (sayi%2==0):
	A.add(sayi)

if (sayi%3==0):
	B.add(sayi)
if (sayi%12==0):
	C.add(sayi)
kesisim= A.intersection(B)-C


print ("A{}",A)
print ("B{}",B)
print ("C{}",C)
print ("A{} kesişim B{}-C{}:",kesisim)