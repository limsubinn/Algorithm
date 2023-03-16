# 프로그래머스 12979: 기지국 설치 - 수정중

def solution(n, stations, w):
    answer = 0
    array = [0] + [1] * n
    k = 1
    t = n+1

    for i in stations:
        if i+w >= n:
            t = i-w
            break
        if i-w < 1:
            k = i+w
            continue
        tmp = array[k:i-w]
        k = i+w+1
        
    tmp = array[k:t]
    print(tmp, k, t)

    return answer

print(solution(11, [4, 11], 1))
print(solution(16, [9], 2))
print(solution(10, [2, 7], 2))