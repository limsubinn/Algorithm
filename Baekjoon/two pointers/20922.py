n, k = map(int, input().split())
a = list(map(int, input().split()))

num = [0] * 200001 # 수열에서 숫자가 나타난 횟수
answer = cnt = 0
j = 0

for i in range(n):
    while j < n and num[a[j]] < k:
        num[a[j]] += 1
        j += 1
        cnt += 1
    answer = max(answer, cnt) # 최댓값 갱신
    cnt -= 1
    num[a[i]] -= 1

print(answer)