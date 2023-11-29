n = int(input())
m = int(input())
data = list(map(int, input().split()))

data.sort()
answer = 0
i, j = 0, n-1

while i < j:
    # 두 합이 m보다 크면 끝값 감소
    if data[i] + data[j] > m:
        j -= 1
    # 두 합이 m보다 작으면 시작값 증가
    elif data[i] + data[j] < m:
        i += 1
    # 두 합이 m일 때 정답 추가 후 시작값, 끝값 조정
    else:
        answer += 1
        i += 1
        j -= 1

print(answer)