n = int(input())

stair = [[0, 0, 0, 0, 0, 0, 0, 0, 0, 0] for _ in range(n+1)]
stair[1] = [0, 1, 1, 1, 1, 1, 1, 1, 1, 1]

for i in range(2, n+1):
    for j in range(10):
         if j == 0:
            stair[i][0] = stair[i-1][1]
         elif j == 9:
            stair[i][9] = stair[i-1][8]
         else:
            stair[i][j] = stair[i-1][j-1] + stair[i-1][j+1]

print(sum(stair[n]) % 1000000000)