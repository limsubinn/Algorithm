import sys

def input():
    return sys.stdin.readline().strip()

s = input()
e = input()

stack = []
for i in range(len(s)):
    # 넣기
    stack.append(s[i])
    # 폭발 문자열이면
    if ''.join(stack[-len(e):]) == e:
        # 빼기
        for _ in range(len(e)):
            stack.pop()

if stack:
    answer = ''.join(stack)
else:
    answer = "FRULA"

print(answer)