# 2805. 농작물 수확하기

T = int(input())

for t in range(1, T+1):
    n = int(input())
    board = [list(map(int, input())) for _ in range(n)]
    
    start = end = n//2
    answer = 0

    for x in range(n):
        for y in range(start, end+1):
            answer += board[x][y]

        if x < n//2:
            start -= 1
            end += 1
        else:
            start += 1
            end -= 1
    
    print(f'#{t} {answer}')