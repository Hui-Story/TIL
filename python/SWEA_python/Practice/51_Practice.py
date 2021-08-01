num_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]

result_1 = filter(lambda x : x%2==0, num_list)

result_2 = map(lambda x : x ** 2, list(result_1))
print(list(result_2))