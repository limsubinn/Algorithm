import sys
sys.setrecursionlimit(1000000)
input = sys.stdin.readline

def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    # 번호 작은 노드가 부모 - 번호 큰 노드가 자식
    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n, m = map(int, input().split())

parent = [0] * (n+1)
for i in range(n+1):
    parent[i] = i

for _ in range(m):
    c, a, b = map(int, input().split())

    if c == 0: # 합집합
        union_parent(parent, a, b)
    else: # 같은 집합인지 확인
        if find_parent(parent, a) == find_parent(parent, b):
            print("YES")
        else:
            print("NO")
