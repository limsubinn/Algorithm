# 프로그래머스 42842: 카펫

def solution(brown, yellow):
    carpet = []
    for i in range(1, int(yellow**0.5)+1):
        # 가능한 가로, 세로의 조합
        if yellow % i == 0:
            # 총 면적은 yellow의 가로+2, 세로+2
            carpet.append([yellow // i + 2, i + 2])
            
    for x, y in carpet:
        if x * y - yellow == brown:
            return [x, y]