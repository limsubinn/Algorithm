import sys

def input():
    return sys.stdin.readline().strip()

def find(res, idx):
    global answer

    if idx == n:
        if res == s:
            answer += 1
        return

    find(res, idx+1) # 합에 포함하는 경우
    find(res+numbers[idx], idx+1) # 합에 포함하지 않는 경우

n, s = map(int, input().split())
numbers = list(map(int, input().split()))

answer = 0
find(0, 0)

# 부분수열의 합이 0이면 원소가 0개인 부분집합이 포함되기 때문에 하나 빼줌
if s == 0:
    answer -= 1

print(answer)