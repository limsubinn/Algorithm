n, k = map(int, input().split())
data = list(map(int, input().split()))

answer = result = sum(data[:k])
for i in range(k, n):
    result += data[i] - data[i-k]
    answer = max(answer, result)

print(answer)