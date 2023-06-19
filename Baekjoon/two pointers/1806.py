n, s = map(int, input().split())
data = list(map(int, input().split()))

start = end = 0
cnt = 1
temp = data[0]
answer = float('INF')

while True:
    # 합이 s 이상인 경우
    # start를 옮기면서 범위를 좁힌다.
    if temp >= s:
        temp -= data[start]
        answer = min(answer, cnt)
        cnt -= 1
        start += 1
    # 합이 s 미만인 경우
    # end를 옮기면서 범위를 늘린다.
    else:
        end += 1
        if end >= n:
            break
        temp += data[end]
        cnt += 1

if answer == float('INF'):
    print(0)
else:
    print(answer)