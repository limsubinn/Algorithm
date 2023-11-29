# 슬라이딩 윈도우

n, x = map(int, input().split())
visitors = list(map(int, input().split()))

# 초기값
result = temp = sum(visitors[:x])
cnt = 1

for i in range(x, n):
    temp += visitors[i] - visitors[i-x] # 누적합 계산

    if result < temp:
        result = temp
        cnt = 1
    elif result == temp:
        cnt += 1

if result == 0:
    print("SAD")
else:
    print(result)
    print(cnt)

'''    
# 투 포인터

n, x = map(int, input().split())
visitors = list(map(int, input().split()))

i = j = 0
temp = result = 0
cnt = 0

for i in range(n):
    # 끝 포인터 이동
    while j-i < x and j < n:
        temp += visitors[j]
        j += 1

    # x일
    if j-i == x:
        if result < temp:
            result = temp
            cnt = 1
        elif result == temp:
            cnt += 1

    # 시작 포인터 값 빼주기
    temp -= visitors[i]

if result == 0:
    print("SAD")
else:
    print(result)
    print(cnt)
'''