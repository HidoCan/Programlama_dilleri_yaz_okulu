
k==0<k<2
a==0<a<2
f(a)
g(a)
h(a)
f(a)<g(a)
g(a)<h(a)
h(a)<f(a)
if (0<a<k):
	if (h(a)<g(a)<f(a)):
		print("Doğru")
	else:
		print("Yanlış")
if (k<a<2):
	if (f(a)<g(a)<h(a)):
		print("Doğru")
	else:
		print("Yanlış")