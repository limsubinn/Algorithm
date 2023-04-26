from itertools import combinations

def odd(n):
    cnt = 0
    for i in n:
        if int(i) % 2 != 0:
            cnt += 1
    return cnt

def command(n, cnt):
    cnt += odd(n)
    if len(n) == 1:
        answer.append(cnt)
    elif len(n) == 2:
        n = int(n[0]) + int(n[1])
        command(str(n), cnt)
    else:
        c = list(combinations(range(1, len(n)), 2)) # 자를 인덱스
        for i, j in c:
            m = int(n[:i]) + int(n[i:j]) + int(n[j:])
            command(str(m), cnt)


n = input()
answer = []
command(n, 0)
print(min(answer), max(answer))