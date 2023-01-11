# 프로그래머스 42862: 체육복

def solution(n, lost, reserve):
    reserve.sort()
    
    nLost = list(set(lost) - set(reserve))
    nReserve = list(set(reserve) - set(lost))
    
    for i in nReserve:
        if i-1 in nLost:
            nLost.remove(i-1)
        elif i+1 in nLost:
            nLost.remove(i+1)
            
    return n - len(nLost)


'''
놓친 부분1) 여벌 체육복을 가진 사람이 도난 당했을 경우 
-> 반복문 안에 if i in lost: lost.remove(i) 추가

놓친 부분2) 위에서 자신의 체육복을 갖지 않고 남에게 빌리는 경우 발생
-> 위의 조건문 제거 & 반복문 시작하기 전에 lost와 reserve의 서로 중복되는 원소들을 지우고 시작
'''