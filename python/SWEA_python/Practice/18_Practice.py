a = ""

for i in range(1, 201):
   if (i % 7) == 0 and (i % 5) != 0:
      a += "%d," % i

print(a[0:len(a)-1])