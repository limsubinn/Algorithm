# 2005. 파스칼의 삼각형

T = int(input())

for t in range(1, T+1):
    n = int(input())

    print(f'#{t}')

    pascal = [[0] * n for _ in range(n)]
    pascal[0][0] = 1 # 첫 번째 줄
    print(pascal[0][0])
    
    for i in range(1, n):
        for j in range(i+1):
            if j == 0:
                pascal[i][j] = 1
            else:
                pascal[i][j] = pascal[i-1][j-1] + pascal[i-1][j]
            print(pascal[i][j], end=' ')
        print()