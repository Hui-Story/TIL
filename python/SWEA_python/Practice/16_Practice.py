a = input()
b = input()

if a == "가위":
    if b == "가위":
        print('Result : Draw')
    elif b == "바위":
        print('Result : Man2 Win!')
    elif b == "보":
        print('Result : Man1 Win!')
elif a == "바위":
    if b == "가위":
        print('Result : Man1 Win!')
    elif b == "바위":
        print('Result : Draw')
    elif b == "보":
        print('Result : Man2 Win!')
elif a == "보":
    if b == "가위":
        print('Result : Man2 Win!')
    elif b == "바위":
        print('Result : Man1 Win!')
    elif b == "보":
        print('Result : Draw')