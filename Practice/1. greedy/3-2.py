n, m, k = map(int, input().split())
num = list(map(int, input().split()))
res = 0

num.sort()
first = num[n-1]
second = num[n-2]

cnt = m // (k + 1) * k + m % (k + 1)    # 가장 큰 수 더하는 횟수
res += cnt * first + (m - cnt) * second # 더하기

print(res)