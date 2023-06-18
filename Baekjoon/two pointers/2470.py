n = int(input())
data = list(map(int, input().split()))

data.sort()
i, j = 0, n-1 # 양쪽 끝에서부터 비교
result = float('INF')

while i < j:
    # 두 용액의 합이 기존값보다 더 0에 가까우면 정답 갱신
    if abs(data[i] + data[j]) < result:
        result = abs(data[i] + data[j])
        answer = [data[i], data[j]]

    # 두 용액의 합이 0보다 작으면 왼쪽 값 증가
    if data[i] + data[j] < 0:
        i += 1
    # 두 용액의 합이 0보다 크면 오른쪽 값 증가
    else:
        j -= 1

print(*answer)