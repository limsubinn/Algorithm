# bottom-up
# 116ms

from collections import deque

def find(A, B):
    queue = deque()
    queue.append([A*2, 2])
    queue.append([int(str(A) + str('1')), 2])

    while queue:
        n, result = queue.popleft()

        if n == B:
            return result
        
        if n > B:
            continue

        queue.append([n*2, result+1])
        queue.append([int(str(n) + str('1')), result+1])

    return -1

A, B = map(int, input().split())
print(find(A, B))

'''
top-down
40ms

def find(A, B):
    answer = 1

    while B > A:
        answer += 1

        if B % 10 == 1:
            B //= 10
        elif B % 2 == 0:
            B //= 2
        else:
            return -1
    
    if B != A:
        return -1
    
    return answer

A, B = map(int,input().split())
print(find(A, B))
'''