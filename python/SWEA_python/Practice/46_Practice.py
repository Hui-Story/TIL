word = 'ADCBBBBCABBCBDACBDCAACDDDCAABABDBCBCBDBDBDDABBAAAAAAADADBDBCBDABADCADC'

n = list(map(lambda x: 4 if x == 'A' else 3 if x == 'B' else 2 if x == 'C' else 1, word))
print(sum(n))