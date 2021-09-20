import math
s1=math.sqrt(5)
s2=math.sqrt(8)
s3=math.sqrt(12)
s4=math.sqrt(18)
s5=math.sqrt(20)
s6=math.sqrt(27)
top=0
liste=[s1,s2,s3,s4,s5,s6]
liste2=[]
for i in liste:
    if s1==i:
        continue
    else:
        a=s1.i
        if isinstance(a,int):
            liste2.append(s1,i)
            liste.remove(s1,i)
for j in liste2:
    top+=j
print(top)