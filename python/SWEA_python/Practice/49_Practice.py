num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result = filter(lambda x : x%2==0, num_list)
print(list(result))