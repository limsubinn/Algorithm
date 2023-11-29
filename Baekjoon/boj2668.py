from collections import deque

def bfs(i, result):
    visited1 = []
    visited2 = []
    
    queue = deque([array[i]])
    visited1.append(i) # 첫째 줄에서 방문한 숫자들
    visited2.append(array[i]) # 둘째 줄에서 방문한 숫자들

    while queue:
        i = queue.popleft()
        visited1.append(i)

        if array[i] not in visited2:
            queue.append(array[i])
            visited2.append(array[i])
    
    # 첫째 줄의 방문한 숫자들과 둘째 줄의 방문한 숫자들이 같은 경우 정답 배열에 추가
    if set(visited1) == set(visited2):
        for i in list(set(visited1)):
            result.append(i)
        result = list(set(result))

n = int(input())

array = [0]
for i in range(1, n+1):
    array.append(int(input()))

result = [] # 뽑힐 정수들을 저장할 배열
for i in range(1, n+1):
    bfs(i, result)
result = list(set(result)) # 중복 제거
result.sort()

print(len(result))
for i in result:
    print(i)