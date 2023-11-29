N, K = map(int, input().split())

card = [[0] * N for _ in range(K+1)]
card[0] = list(map(int, input().split()))
mix = list(map(int, input().split()))

for k in range(K):
    for n in range(N):
        card[k+1][mix[n]-1] = card[k][n]

for c in card[-1]:
    print(c, end=' ')