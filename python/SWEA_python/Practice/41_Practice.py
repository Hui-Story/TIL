numbers = list(map(int, input().split(',')))

def square(n):
    result = n ** 2
    print(f'square({n}) => {result}')

for number in numbers:
    square(number)