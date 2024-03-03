# 백준 19539: 사과나무

n = int(input())
heights = list(map(int, input().split()))

if sum(heights) % 3 != 0:
    print("NO")
else:
    # 나무가 모두 자라나는 데 걸리는 시간
    time = sum(heights) // 3

    # 나무 하나를 2만큼 성장시키는 물뿌리개를 사용할 수 있는 횟수
    cnt = 0
    for h in heights:
        cnt += h // 2

    if cnt < time:
        print("NO")
    else:
        print("YES")
