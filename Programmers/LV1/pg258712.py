# 프로그래머스 258712: 가장 많이 받은 선물

def solution(friends, gifts):
    size = len(friends)

    # 인덱싱
    dic = {}
    for i, friend in enumerate(friends):
        dic[friend] = i

    # 선물을 주고받은 기록
    records = [[0] * size for _ in range(size)]
    f = [0] * size  # 준 선물
    t = [0] * size  # 받은 선물
    for gift in gifts:
        a, b = gift.split()
        a = dic[a]
        b = dic[b]
        records[a][b] += 1
        f[a] += 1
        t[b] += 1

    # 선물 지수
    idx = [0] * size
    for i in range(size):
        idx[i] = f[i] - t[i]

    # 다음달에 받을 선물의 개수
    result = [0] * size
    for i in range(size):
        for j in range(i + 1, size):
            if i == j:
                continue
            if records[i][j] > records[j][i]:
                result[i] += 1
            elif records[i][j] < records[j][i]:
                result[j] += 1
            else:
                if idx[i] > idx[j]:
                    result[i] += 1
                elif idx[i] < idx[j]:
                    result[j] += 1

    return max(result)