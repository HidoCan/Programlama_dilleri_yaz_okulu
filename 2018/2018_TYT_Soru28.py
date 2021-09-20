from itertools import combinations_with_replacement

combi = combinations_with_replacement(['a', 'b', 'c', 'd'], 2)


for c in list(combi):
   print(c)
