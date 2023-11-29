from collections import deque

def makeList(info):
    melody = [info[0]]
    queue = deque(list(info[1:]))
    while queue:
        q = queue.popleft()
        if q == '#':
            melody[-1] += q
        else:
            melody.append(q)
    return melody
    
def solution(m, musicinfos):
    answer = []
    m = list(m)
    order = 0
    
    for i in musicinfos:
        i = i.split(',')

        # 재생 시간 계산
        start = int(i[0][:2]) * 60 + int(i[0][3:])
        end = int(i[1][:2]) * 60 + int(i[1][3:])

        # 멜로디 리스트로 변환
        music = makeList(i[3])
        m = makeList(m)
    
        # 악보 만들기 (재생 시간만큼 자르거나 붙인다.)
        time = end - start
        play = []
        while True:
            if time <= len(music):
                for j in music[:time]:
                    play.append(j)
                break
            for j in music:
                play.append(j)
            time -= len(music)

        # m이 악보에 포함되어 있으면 정답 배열에 추가
        for j in range(len(m), len(play)+1):
            if play[j-len(m):j] == m:
                answer.append([len(play), order, i[2]])
                order += 1
                break
    
    if not answer:
        # 큰 따옴표로 묶었을 때 tc29 실패.. 작은 따옴표로 바꾸니까 통과됐는데 무슨 차이일까...? 황당하다
        return '(None)'
    
    # 재생 시간 긴 순 -> 먼저 입력된 순으로 정렬
    answer.sort(key = lambda x:(-x[0], x[1]))
    return answer[0][2]