import sys
sys.setrecursionlimit(10**9)

class Node:
    def __init__(self, data, left, right):
        self.data = data
        self.left = left
        self.right = right

def input():
    return sys.stdin.readline().strip()

def inorder(node):
    if node.left:
        inorder(tree[node.left])
    order.append(node.data)
    if node.right:
        inorder(tree[node.right])

def similar_inorder(node, end):
    global result, answer

    if node.left and not visited[node.left]:
        result += 1
        visited[node.left] = True
        similar_inorder(tree[node.left], end)
    if node.right and not visited[node.right]:
        result += 1
        visited[node.right] = True
        similar_inorder(tree[node.right], end)
    if node.data == end:
        answer = result
        return answer
    result += 1

n = int(input())
tree = {}
visited = [False] * (n+1)

for i in range(n):
    a, b, c = map(int, input().split())
    if b == -1:
        b = None
    if c == -1:
        c = None
    tree[a] = Node(a, b, c)

order = []
inorder(tree[1]) # 중위 순회
end = order[-1] # 중위 순회의 끝값

global result, answer
result = 0
similar_inorder(tree[1], end) # 유사 중위 순회

print(answer)