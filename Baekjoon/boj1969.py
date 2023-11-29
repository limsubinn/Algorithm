import sys

def input():
    return sys.stdin.readline().strip()

n, m = map(int, input().split())
dna = [list(input()) for _ in range(n)]

answer = ''
cnt = 0
for j in range(m):
    # 각 열의 문자 개수 카운팅
    dic = {}
    for i in range(n):
        k = dna[i][j]
        if k in dic:
            dic[k] += 1
        else:
            dic[k] = 1
    # value(카운트) 내림차순, key(문자) 오름차순으로 정렬
    dic = sorted(dic.items(), key = lambda x:(-x[1], x[0]))
    # 딕셔너리의 첫 번째 요소
    d = next(iter(dic))
    # 정답 추가
    answer += d[0]
    cnt += n - d[1]

print(answer)
print(cnt)