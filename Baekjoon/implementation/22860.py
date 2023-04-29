import sys
sys.setrecursionlimit(10**9)

def input():
    return sys.stdin.readline().strip()

def find(name):
    for i in folder[name]:
        find(i)
    for i in file[name]:
        result.append(i)

n, m = map(int, input().split())

folder, file = {}, {}
for i in range(n+m):
    p, f, c = input().split()
    if c == '0':
        if p in file:
            file[p].append(f)
        else:
            file[p] = [f]
    else:
        if p in folder:
            folder[p].append(f)
        else:
            folder[p] = [f]
        if f not in folder:
            folder[f] = []
        if f not in file:
            file[f] = []
    if p not in file:
        file[p] = []


q = int(input())
for i in range(q):
    name = input()
    if '/' in name:
        name = name.split('/')[-1]

    result = []
    find(name)

    cnt1 = len(set(result))
    cnt2 = len(result)
    print(cnt1, cnt2)