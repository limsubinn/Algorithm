import sys

def input():
    return sys.stdin.readline().strip()

def alpha_to_num(alpha):
    return ord(alpha) - 97

def find(start, cnt):
    global answer

    # 알파벳을 k개 뽑았을 때
    if cnt == k:
        result = 0
        # 단어 순회하면서 가르침 여부 판단
        for word in words:
            for w in word:
                # 가르칠 수 없는 경우
                if not visited[alpha_to_num(w)]:
                    break
            # 가르칠 수 있는 경우
            else:
                result += 1
        # 최댓값 갱신
        answer = max(answer, result)

    # 알파벳 뽑기
    for i in range(start, 26):
        if visited[i]:
            continue
        visited[i] = True
        find(i, cnt+1)
        visited[i] = False

n, k = map(int, input().split())
words = [input()[4:-4] for _ in range(n)] # anta, tica 떼기

# 가르칠 수 없을 경우
if k < 5:
    print(0)
    exit()

# 알파벳 방문 리스트
visited = [False] * 26
for alpha in ('a', 'n', 't', 'i', 'c'):
    visited[alpha_to_num(alpha)] = True

answer = 0
find(0, 5)
print(answer)