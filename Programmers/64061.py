# 프로그래머스 64061: 크레인 인형뽑기 게임 (2019 카카오 개발자 겨울 인턴십)

def solution(board, moves):
    answer = 0
    temp = [0 for i in range(len(board))]
    basket = []
    
    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[j][i] != 0:
                temp[i] = j
                break
    
    for i in moves:
        if temp[i-1] < len(board[0]):
            basket.append(board[temp[i-1]][i-1])
            temp[i-1] += 1
        if len(basket) > 1 and basket[-2] == basket[-1]:
            basket.pop()
            basket.pop()
            answer += 2
        
    return answer