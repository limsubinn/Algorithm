# 그래프 이론
# 실전 문제2. 커리큘럼

from collections import deque
import copy

n = int(input())

indegree = [0] * (n+1) # 모든 노드에 대한 진입차수
graph = [[] for i in range(n+1)] # 모든 간선에 대한 정보를 담은 리스트
time = [0] * (n+1) # 강의 시간

for i in range(1, n+1):
    data = list(map(int, input().split()))
    time[i] = data[0] # 강의 시간
    for j in data[1:-1]: # 선수 강의
        indegree[i] += 1
        graph[j].append(i)

def topology_sort():
    # 알고리즘 수행 결과를 담을 리스트
    # 리스트의 경우, 단순히 대입 연산을 하면 값이 변경될 때 문제가 발생할 수 있기 때문에 리스트의 값을 복제해서 사용 -> deepcopy
    res = copy.deepcopy(time)
    # 큐 -> deque
    q = deque()

    for i in range(1, n+1):
        if indegree[i] == 0:
            q.append(i)

    while q:
        now = q.popleft()
        for i in graph[now]:
            indegree[i] -= 1
            res[i] = max(res[i], res[now] + time[i])
            if indegree[i] == 0:
                q.append(i)

    for i in range(1, n+1):
        print(res[i])

topology_sort()
