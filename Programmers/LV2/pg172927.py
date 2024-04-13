# 프로그래머스 172927: 광물 캐기

import heapq

def make_queue(s, minerals):
    dic = {"diamond": 25, "iron": 5, "stone": 1}

    queue = []
    tq = []
    ts = 0

    for i in range(len(minerals)):
        if i >= s:  # 더이상 광물을 캘 수 없는 경우
            break

        tq.append(minerals[i])
        ts += dic[minerals[i]]

        # 한 묶음
        if i % 5 == 4:
            heapq.heappush(queue, (-ts, tq))
            tq = []
            ts = 0

    # 남은 광물
    if tq:
        heapq.heappush(queue, (-ts, tq))

    return queue

def cal(pick, mineral):
    # 다이아몬드 곡괭이
    if pick == 0:
        return 1
    # 철 곡괭이
    if pick == 1:
        if mineral == "diamond":
            return 5
        return 1
    # 돌 곡괭이
    if mineral == "diamond":
        return 25
    if mineral == "iron":
        return 5
    return 1

def solution(picks, minerals):
    queue = make_queue(sum(picks) * 5, minerals)
    answer = 0

    for i in range(len(picks)):
        for j in range(picks[i]):
            # 더이상 캘 광물이 없는 경우
            if not queue:
                return answer
            # 한 묶음 빼기
            tq = heapq.heappop(queue)[1]
            # 피로도 더하기
            for q in tq:
                answer += cal(i, q)

    return answer