a=0<a<1
b=f(g(a))
c=g(f(a))
a=0.5
f(g(a))=2.5
b=f(2.5)=1.7
g(f(a))=1.5
c=g(1.5)=2.5
if (a<b):
	if (b<c):
		print("a<b<c")
	else:
		print("a<c<b")
if (a<c):
	print("b<a<c")
else:
	print("b<c<a")