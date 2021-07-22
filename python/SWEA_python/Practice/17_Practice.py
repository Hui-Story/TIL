a = input()

if a.isupper():
    print('%s(ASCII: %d) => %s(ASCII: %d)' %(a, ord(a), a.lower(), ord(a.lower())))
elif a.islower():
    print('%s(ASCII: %d) => %s(ASCII: %d)' %(a, ord(a), a.upper(), ord(a.upper())))
else:
    print(a)