from itertools import permutations

n = int(input())
numbers = list(permutations(list(map(str, range(1, 10))), 3)) # 가능한 숫자의 조합

for _ in range(n):
    num, strike, ball = map(int, input().split())
    num = list(str(num))
    cnt = 0

    for i in range(len(numbers)):
        s, b = 0, 0
        i -= cnt

        for j in range(3):
            if numbers[i][j] == num[j]: # 스트라이크
                s += 1
                continue
            if num[j] in numbers[i]: # 볼
                b += 1
        
        # 입력된 스트라이크, 볼의 수와 계산한 스트라이크, 볼의 수가 다르면 제거
        if strike != s or ball != b:
            numbers.remove(numbers[i])
            cnt += 1

print(len(numbers))