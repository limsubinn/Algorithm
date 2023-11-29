n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = sorted(a + b)
print(*result)

'''
# 투 포인터 이용

n, m = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))

result = [0] * (n + m)
i = j = k = 0

while i < n or j < m:
    if j >= m or (i < n and a[i] < b[j]):
        result[k] = a[i]
        i += 1
    else:
        result[k] = b[j]
        j += 1
    k += 1

print(*result)
'''
