a = ""

for i in range(100, 301):
   if (i % 2) == 0 and ((i // 10) % 2 == 0) and ((i // 100) % 2 == 0):
      a += "%d," % i

print(a[0:len(a)-1])