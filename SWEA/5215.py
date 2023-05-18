# 5215. 햄버거 다이어트

def dfs(i, score, cal):
    global answer

    # 칼로리가 제한 칼로리를 넘으면 종료
    if cal > l:
        return
    
    # 최댓값 갱신
    answer = max(answer, score)
    
    # 모든 재료를 탐색했으면 종료
    if i == n:
        return
    
    s, c = ingredient[i]

    # 재료를 사용하는 경우
    dfs(i+1, score + s, cal + c)
    # 재료를 사용하지 않는 경우
    dfs(i+1, score, cal)

T = int(input())

for t in range(1, T+1):
    n, l = map(int, input().split())
    ingredient = [list(map(int, input().split())) for _ in range(n)]

    answer = 0
    dfs(0, 0, 0)

    print(f'#{t} {answer}')