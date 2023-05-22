from itertools import combinations

n, m = map(int, input().split())
preferences = [list(map(int, input().split())) for _ in range(n)]

combi = list(combinations(range(m), 3)) # 치킨 3개 뽑기
answer = 0

for a, b, c in combi:
    res = 0
    for i in range(n): # 최대 선호도 구하기
        res += max(preferences[i][a], preferences[i][b], preferences[i][c])
    answer = max(answer, res) # 최댓값 갱신

print(answer)