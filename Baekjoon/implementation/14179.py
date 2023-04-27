def solution(array):
    idx = 0
    answer = 0

    for i in range(1, len(array)):
        if array[idx] <= array[i]:
            idx = i
        else:
            answer += array[idx] - array[i]
        
    return answer

h, w = map(int, input().split())
blocks = list(map(int, input().split()))

m = blocks.index(max(blocks))

answer = 0
answer += solution(blocks[:m])
answer += solution(blocks[-1:m:-1])
print(answer)