import sys

def input():
    return sys.stdin.readline().strip()

# 문자 -> 숫자 맵핑
def s2n(s):
    s = ord(s)
    if s <= 90:
        return s - 65
    return s - 71

# 숫자 -> 문자 맵핑
def n2s(n):
    if n <= 25:
        return chr(n + 65)
    return chr(n + 71)

graph = [[False] * 52 for _ in range(52)]

n = int(input())
for _ in range(n):
    a, b, c = input().split()
    graph[s2n(a)][s2n(c)] = True

for k in range(52):
    for i in range(52):
        for j in range(52):
            # 거쳐가는 경로가 존재할 경우
            if graph[i][k] and graph[k][j]:
                graph[i][j] = True

cnt = 0
result = []
for i in range(52):
    for j in range(52):
        # 경로가 존재할 경우 (자기 자신으로 가는 경우 제외)
        if graph[i][j] and i != j:
            cnt += 1
            result.append(f'{n2s(i)} => {n2s(j)}')

print(cnt)
for res in result:
    print(res)