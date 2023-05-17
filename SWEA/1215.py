# 1215. 회문1

def search_row():
    answer = 0
    for i in range(8):
        for j in range(8-n+1):
            w = words[i][j:j+n]
            if w == w[::-1]:
                answer += 1
    return answer

for t in range(1, 11):
    n = int(input())
    words = [list(input()) for _ in range(8)]

    # 가로
    answer = search_row()
    # 세로
    words = [list(i) for i in zip(*words)]
    answer += search_row()

    print(f'#{t} {answer}')