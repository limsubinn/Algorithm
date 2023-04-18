N = int(input())
K = int(input())
sensor = list(map(int, input().split()))

sensor.sort()
diff = []
for i in range(1, N):
    diff.append(sensor[i] - sensor[i-1]) # 각 센서의 차이값

diff.sort()
for i in range(K-1): # 가장 차이가 큰 값부터 K-1개 빼주기
    if not diff:
        break
    diff.pop()

answer = sum(diff)
print(answer)