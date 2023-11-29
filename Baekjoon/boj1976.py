def find_parent(parent, x):
    if parent[x] != x:
        parent[x] = find_parent(parent, parent[x])
    return parent[x]

def union_parent(parent, a, b):
    a = find_parent(parent, a)
    b = find_parent(parent, b)

    if a < b:
        parent[b] = a
    else:
        parent[a] = b


n = int(input())
m = int(input())

parent = [0] * (n+1)
for i in range(1, n+1):
    parent[i] = i

cities = []
for i in range(n):
    cities.append(list(map(int, input().split())))
    for j in range(n):
        if cities[i][j] == 1:
            union_parent(parent, i+1, j+1)


plan = list(map(int, input().split()))
plan_set = set(plan) # 중복 제거

check = find_parent(parent, plan[0])
for i in plan_set:
    if find_parent(parent, i) != check:
        print("NO")
        exit(0)
print("YES")