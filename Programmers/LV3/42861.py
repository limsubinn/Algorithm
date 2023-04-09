# 프로그래머스 42861: 섬 연결하기
# 크루스칼 알고리즘

def find(parent, x):
    if parent[x] != x:
        parent[x] = find(parent, parent[x])
    return parent[x]

def union(parent, a, b):
    a = find(parent, a)
    b = find(parent, b)
    if a > b:
        parent[a] = b
    else:
        parent[b] = a

def solution(n, costs):
    answer = 0
    parent = [i for i in range(n)] # 부모 테이블 초기화
    costs.sort(key=lambda x:x[2]) # cost를 기준으로 정렬
    
    for a, b, c in costs:
        if find(parent, a) != find(parent, b):
            union(parent, a, b)
            answer += c

    return answer