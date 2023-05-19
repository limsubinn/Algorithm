# 1860. 진기의 최고급 붕어빵

T = int(input())

for t in range(1, T+1):
    n, m, k = map(int, input().split())
    people = list(map(int, input().split()))

    people.sort()
    answer = 'Possible'
    cook = [0]
    p = 1

    for person in people:
        for i in range(p, person+1):
            cook.append(cook[-1])
            # m초마다 붕어빵 만들기
            if i % m == 0:
                cook[-1] += k
        # 붕어빵 제공
        cook[-1] -= 1
        # 붕어빵을 제공할 수 없는 경우
        if cook[-1] < 0:
            answer = 'Impossible'
            break
        p = person + 1

    print(f'#{t} {answer}')