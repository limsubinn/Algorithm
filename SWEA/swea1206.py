# 1206. View

def view(i):
    # 최댓값
    result = 255
    # 양쪽 2칸 확인
    for j in [-1, -2, 1, 2]:
        # 조망권 확보를 실패하는 경우
        if building[i+j] >= building[i]:
            return 0
        # 최솟값 갱신
        result = min(result, building[i] - building[i+j])
    return result

for t in range(1, 11):
    n = int(input())
    building = list(map(int, input().split()))

    answer = 0
    for i in range(2, n-2):
        answer += view(i)
    print(f'#{t} {answer}')