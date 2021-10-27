import sys
input = sys.stdin.readline

N = int(input())
word_cnt = [[[i, 0] for i in range(10)] for _ in range(12)]  # 각 자리수에 알파벳이 몇 번 나오는지 카운트
used = [0]*10  # 숫자가 대입된 알파벳 체크
not_zero = [0]*10  # 0 이 될 수 없는 알파벳 True로 체크 (가장 앞에 오는 알파벳)
word_check = [0]*10  # 사용된 알파벳 체크
max_word_len = 0  # 가장 긴 자리수
result = 0

for _ in range(N):
    inp = str(input().strip())
    max_word_len = max(max_word_len, len(inp))
    for i in range(len(inp)):
        # 가장 앞에 오는 알파벳 not_zero 체크
        if i == 0:
            not_zero[ord(inp[i])-65] = 1
        # 각 자리수에 알파벳 A~J 를 0~9 인덱스로 개수 체크
        word_cnt[len(inp)-1-i][ord(inp[i])-65][1] += 1
        # 사용된 알파벳은 word_check 체크
        word_check[ord(inp[i])-65] = 1

not_zero_cnt = sum(not_zero)  # 0 이 될 수 없는 알파벳 개수
word_check = sum(word_check)  # 사용된 알파벳 개수로 변경

# 숫자를 큰 수부터 각 알파벳에 대입하면서 최대가 될 수 있는 경우를 탐색
for num in range(9, -1, -1):
    max_sum = -1
    now_word = 0
    # 현재 숫자를 알파벳에 하나씩 대입
    for word_ord in range(10):
        # 이미 숫자가 대입되어 있는 알파벳일 경우 continue
        if used[word_ord]:
            continue
        # 현재 숫자가 0 이 아니고
        # 0 이 될 수 없는 알파벳이 이후 남아있는 숫자만큼 남아있고
        # 현재 알파벳이 0 이 될 수 있는 경우
        # continue (남은 알파벳 중 유일하게 0 이 될 수 있음)
        if num and not_zero_cnt == num and not not_zero[word_ord]:
            continue
        # tmp에 현재 알파벳에 대입했을 경우의 합을 저장
        tmp = 0
        for i in range(max_word_len):
            tmp += num * word_cnt[i][word_ord][1] * (10**i)
        # tmp가 최대일 경우 max_sum에 저장하고, 현재 알파벳을 저장
        if tmp > max_sum:
            max_sum = tmp
            now_word = word_ord
    # 알파벳에 대입하여 가장 높은 경우 그 알파벳에 숫자를 대입
    result += max_sum
    used[now_word] = 1
    # 남아있는 0 이 될 수 없는 알파벳의 개수 업데이트
    if not_zero[now_word]:
        not_zero_cnt -= 1

print(result)