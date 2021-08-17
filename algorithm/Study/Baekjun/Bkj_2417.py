n = int(input())

def binary(low, high, n):
    while low <= high:
        middle = (low + high) // 2
        if (high-low) <= 1:
            if low**2 == n:
                return low
            else:
                return high
        elif n < middle**2:
            high = middle
        else:
            low = middle
    return

print(int(binary(0, 2**32, n)))