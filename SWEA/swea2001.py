# 2001. 파리 퇴치

def find(x, y):
    cnt = 0
    for i in range(m):
        cnt += sum(flies[x+i][y:y+m])
    return cnt

t = int(input())

for test_case in range(1, t+1):
    n, m = map(int, input().split())
    flies = [list(map(int, input().split())) for _ in range(n)]

    answer = 0
    for i in range(n-m+1):
        for j in range(n-m+1):
            # 파리채 내리친 결과
            cnt = find(i, j)
            # 최댓값 갱신
            if cnt >= answer:
                answer = cnt
    print(f'#{test_case} {answer}')