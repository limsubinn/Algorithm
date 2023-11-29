import sys

def input():
    return sys.stdin.readline().strip()

def dfs(i, value):
    global answer

    if i == n-1:
        answer = max(answer, int(value))
        return

    if i+2 < n: # 괄호 X
        dfs(i+2, operator(value, expression[i+1], expression[i+2]))

    if i+4 < n: # 괄호 O
        dfs(i+4, operator(value, expression[i+1], operator(expression[i+2], expression[i+3], expression[i+4])))

def operator(num1, op, num2):
    if op == '+':
        return str(int(num1) + int(num2))
    if op == '-':
        return str(int(num1) - int(num2))
    return str(int(num1) * int(num2))

n = int(input())
expression = list(input())
answer = -float('INF')

dfs(0, expression[0])
print(answer)