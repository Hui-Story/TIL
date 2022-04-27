def dfs(n):
    global answer
    if n == N:
        print(answer)
        return True
    for num in ['1', '2', '3']:
        if check(answer + num):
            answer += num
            if dfs(n + 1):
                return True
            answer = answer[:-1]
    return False

def check(nums):
    l = len(nums) // 2
    for i in range(1, l + 1):
        if nums[-i:] == nums[-i * 2:-i]:
            return False
    return True

N = int(input())
answer = '1'

dfs(1)