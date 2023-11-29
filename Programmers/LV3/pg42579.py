# 프로그래머스 42579: 베스트앨범

from collections import deque

def solution(genres, plays):
    answer = []
    dic = {} # 장르별 고유번호를 저장할 딕셔너리
    play = {} # 장르별 총 재생횟수를 저장할 딕셔너리

    for i in range(len(genres)):
        g = genres[i]
        p = plays[i]

        if g in dic:
            dic[g].append(i)
            play[g] += p
            continue

        dic[g] = [i]
        play[g] = p

    # 재생횟수가 많은 순으로 장르 정렬
    play = dict(sorted(play.items(), key=lambda x:x[1], reverse=True))

    for key in play:
        # 장르 내에서 재생횟수가 많은 순으로 고유번호 정렬 
        # (값이 같을 경우 인덱스가 작은 순으로 자동으로 정렬된다.)
        d = deque(sorted(dic[key], key=lambda x:plays[x], reverse=True))

        # 정답 배열에 2개씩 추가
        answer.append(d.popleft())
        if d:
            answer.append(d.popleft())
    
    return answer