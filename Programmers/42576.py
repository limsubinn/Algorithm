# 프로그래머스 42576: 완주하지 못한 선수

def solution(participant, completion):
    participant.sort()
    completion.sort()
    
    for i in range(len(completion)):
        if participant[i] != completion[i]:
            return participant[i]
    
    return participant[-1]

    '''
    두 리스트를 모두 정렬했을 때,
    같은 인덱스에서 서로 다른 요소를 갖고 있다면 해당 인덱스가 완주하지 못한 선수가 될 것이다.
    '''