list = [1, 2, 3, 4, 3, 2, 1]
new_list = []

def dedupl(list):
    for number in list:
        if number not in new_list:
            new_list.append(number)
    return new_list

print(list)
print(dedupl(list))