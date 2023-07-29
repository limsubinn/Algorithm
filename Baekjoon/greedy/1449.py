n, l = map(int, input().split())
places = list(map(int, input().split()))

places.sort()
start = places[0]
answer = 1

for place in places[1:]:
    # 물이 새는 위치가 테이프의 범위 내에 없으면 테이프 추가
    if place not in range(start, start+l):
        start = place
        answer += 1

print(answer)