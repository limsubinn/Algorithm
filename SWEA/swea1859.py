# 1859. 백만 장자 프로젝트

t = int(input())

for i in range(1, t+1):
    n = int(input())
    array = list(map(int, input().split()))

    m = 0 # 최댓값
    answer = 0

    for j in array[::-1]:
        if j >= m: # 최댓값 갱신
            m = j
        else: # 정답 추가
            answer += m - j

    print(f'#{i} {answer}')