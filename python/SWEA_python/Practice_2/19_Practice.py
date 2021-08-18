tup = (1,2,3,4,5,6,7,8,9,10)

result1 = ()
result2 = ()

for i in range(len(tup)):
    if i < (len(tup) / 2):
        result1 += (tup[i],)
    else:
        result2 += (tup[i],)

print(result1)
print(result2)